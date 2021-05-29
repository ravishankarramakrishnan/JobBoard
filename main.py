# Our Base/Core FastAPI will be present

# Importing Libraries
from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base


# Define a Function to Create Tables
def create_tables():
    # The below code is used to connect FastAPI to Database Engine
    # DB will be Created everytime we start a process (Database will stay intact)
    Base.metadata.create_all(bind=engine)


# Define a Function to Start the Application
def start_application():
    # Initialize FastAPI
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # Create Tables
    create_tables()
    # Return App
    return app


# Define App
app = start_application()


# Create Routes
@app.get('/')
def hello_api():
    return {"detail": "Hello World"}
