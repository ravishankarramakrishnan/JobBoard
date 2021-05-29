# We connect to PostGRES data, from config.py using this file
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

# If you want to use SqlAlchemy Engine

# Define SQLAlchemy Database URL
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

"""
# If you want an Easy/Simpler way, do below -> Sqlite doesnt support Multithreading (It is in local system)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
"""


# Dependency Injection -> For test database
def get_db() -> Generator:
    """This Function would return a Generator"""
    try:
        # Create an Object of Session Local
        db = SessionLocal()
        # If No Problem
        yield db
    finally:
        # Whatever happens, Close the DB session
        db.close()

# Create SessionLocal - to represent actual db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
