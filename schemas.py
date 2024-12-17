# schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema for creating a book
class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    description: Optional[str] = None

# Schema for returning book details
class Book(BaseModel):
    id: int
    title: str
    author: str
    published_date: datetime
    isbn: str
    description: Optional[str] = None

    class Config:
        orm_mode = True  # Enable ORM support
