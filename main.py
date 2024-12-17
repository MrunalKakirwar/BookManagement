# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine

# Initialize FastAPI app
app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to the Book Management API!"}


# Dependency for the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to get all books
@app.get("/books", response_model=List[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# Route to create a new book
@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Route to get a book by ID
@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Route to update a book
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

# Route to delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"detail": "Book deleted successfully"}
