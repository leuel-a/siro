from typing import Dict
from pydantic import BaseModel, Field as PydanticField
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    """
    Base model for user data (shared fields).

    :param name: The user's name (indexed for faster lookup).
    :param email: The user's unique email address.
    :param password: The user's hashed password.
    """
    name: str = Field(index=True)
    email: str = Field(unique=True)


class UserLogin(BaseModel):
    """
    Data Transfer Object (DTO) for login a user

    :param email: The user's email address
    :param password: The user's hashed password
    """
    email: str = PydanticField()
    password: str = PydanticField()


class UserCreate(UserBase):
    """
    Data Transfer Object (DTO) for creating a new user.

    Inherits:
        name, and email fields from UserBase.
    """
    password: str


class UserRead(UserBase):
    """
    Data Transfer Object (DTO) for reading a user.

    Inherits:
        name, and email fields from UserBase.
    """
    id: int
    pass


class User(UserBase, table=True):
    """
    Database model for a user with an auto-incrementing primary key.

    :param id: The user's unique ID (primary key).
    Inherits all fields from UserBase.
    """
    __table_args__ = {"extend_existing": True}

    id: int | None = Field(default=None, primary_key=True)
    password: str


    def to_dict(self) -> Dict:
        """Returns the dictionary representation of a user"""
        user_dict = {}

        for key, value in self.__dict__.items():
            if key != "password":
                user_dict[key] = value
        return user_dict


