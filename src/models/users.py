from typing import Annotated
from sqlmodel import Field, Session, SQLModel

class UserBase(SQLModel):
    name: str = Field(index=True)
    email: str = Field(unique=True)
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
