from fastapi import APIRouter

# Custom Imports
from apis.version1 import route_users

# Create an Instance of APIRouter
api_router = APIRouter()

# Include Routes
api_router.include_router(route_users.router,
                          prefix="/user",
                          tags=["users"]
                          )
