from typing import List

from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, HTTPException

from src.lib.db import SessionDep
from src.models.user import UserRead, UserCreate
from src.config.http_status import HTTPStatus
from src.services.user_service import create_user, get_users as get_users_service

router = APIRouter()


@router.get('', response_model=List[UserRead])
async def get_users(session: SessionDep):
    """Get all uers from the database"""
    users = get_users_service(session)
    return users


@router.post('', response_model=UserRead)
async def create_users(user: UserCreate, session: SessionDep):
    """Creates a new user"""
    try:
        user_created = create_user(user, session)
        return user_created
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Failed to create user"
        ) from e

