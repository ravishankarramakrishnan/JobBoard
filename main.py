# Our Base/Core FastAPI will be present

# Importing Libraries
from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
# from apis.version1.route_users import router
from apis.base import api_router


# Define a Function to Create Tables
def create_tables():
    # The below code is used to connect FastAPI to Database Engine
    # DB will be Created everytime we start a process (Database will stay intact)
    Base.metadata.create_all(bind=engine)


# Create a function to Include Router
def include_router(app):
    app.include_router(api_router)


# Define a Function to Start the Application
def start_application():
    # Initialize FastAPI
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # Create Tables
    create_tables()
    # Include Router in the Application
    # app.include_router(router)
    include_router(app)
    # Return App
    return app


# Define App
app = start_application()


# Create Routes
@app.get('/')
def hello_api():
    return {"detail": "Hello World"}
