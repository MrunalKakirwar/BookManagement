# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define MySQL Database URL
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/book_management"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base for our models
Base = declarative_base()
