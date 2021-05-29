# These are used for Pydantic Schemas / Data Validations
from typing import Optional
from pydantic import BaseModel, EmailStr


# Create Pydentic Model that inherits from Base Model -> Validates on User Creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Create new Class to secure the Web-App. Not show unnecessary fields in json
class ShowUser(BaseModel):
    username: str
    email: str
    is_active: bool

    # Return it - Convert to Dictionary
    class Config():
        # Keep ORM Mode as true - Required for Pydantic to respond filtered results
        orm_mode = True
