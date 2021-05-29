# Our Base/Core FastAPI will be present

# Importing Libraries
from fastapi import FastAPI
from core.config import settings



# Initialize FastAPI
app = FastAPI(title= settings.PROJECT_TITLE, version= settings.PROJECT_VERSION)


# Create Routes
@app.get('/')
def hello_api():
    return {"detail": "Hello World"}