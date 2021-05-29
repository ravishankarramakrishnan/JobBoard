# These are used for Pydantic Schemas / Data Validations
from typing import Optional
from pydantic import BaseModel, EmailStr


# Create Pydentic Model that inherits from Base Model -> Validates on User Creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str