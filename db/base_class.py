# This will act as Base Class / Parent Class for other SQLAlchemy Classes
from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """This acts as Parent class for every SQLAlchemy ORM Class"""
    """ ID should be in All Classes. It automatically creates id for all classes """
    id: Any
    __name__: str

    # Define a Function to Automatically generate Table Name from a Class Name.Create a Method
    @declared_attr
    def __tablename__(cls) -> str:
        """ It takes the Class Name and Returns a String """
        return cls.__name__.lower()
