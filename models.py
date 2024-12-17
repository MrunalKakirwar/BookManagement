# models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Define the Book model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each book
    title = Column(String(255), nullable=False)         # Book title
    author = Column(String(255), nullable=False)        # Book author
    published_date = Column(DateTime, default=datetime.utcnow)  # Date of publication
    isbn = Column(String(13), unique=True, nullable=False)      # ISBN number
    description = Column(String(500))                  # Book description
