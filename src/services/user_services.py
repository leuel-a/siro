from sqlmodel import select

from models import User, UserCreate
from lib.db import SessionDep
from lib.utils import hash_password


def get_users(session: SessionDep):
    """
    Retrieve all User records from the database.

    :param session: The database session dependency.
    :return: A list of all users in the database.
    """
    users = session.exec(select(User)).all()
    return [user.to_dict() for user in users]



def create_user(user: UserCreate, session: SessionDep):
    """
    Add a new user to the database.

    :param user: The user instance to create.
    :param session: The database session dependency.
    :return: The newly created user with updated fields.
    """
    user.password = hash_password(user.password)
    user_to_db = User(name=user.name, password=user.password, email=user.email)

    session.add(user_to_db)
    session.commit()
    session.refresh(user_to_db)

    return user_to_db.to_dict()

