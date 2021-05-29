# Depends is used to tell about dependency
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Custom Module Imports| UserCreate -> Contains only Validations for username, email and pwd
from schemas.users import UserCreate, ShowUser
# get_db is used to patch the Database Sessions - Dependency Injection
from db.session import get_db
from db.repository.users import create_new_user


# Register New Router
router = APIRouter()


# Create new Endpoint - db has a dependency
# @router.post('/users') - Not required as we have prefix in apis - base.py
# Pydentic will fill results on inputs of response_model
@router.post('/', response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user
