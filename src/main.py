#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()

from typing import List, Dict
from contextlib import asynccontextmanager

import uvicorn
from sqlmodel import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import FastAPI, HTTPException

from models import UserCreate, UserRead
from lib.db import init_db, SessionDep
from config.app_settings import settings
from config.http_status import HTTPStatus
from services.user_services import create_user, get_users



@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)



@app.get('/checkhealth')
async def checkhealth(session: SessionDep) -> Dict[str, bool]:
    try:
        session.exec(select(1))
        return {'db': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")


@app.get("/users", response_model=List[UserRead])
async def read_users(session: SessionDep):
    """Get all users from the database"""
    users = get_users(session)
    return users


@app.post('/users', response_model=UserRead)
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


if __name__ == "__main__":
    uvicorn.run(
            "main:app",
            host=settings.app_host,
            port=settings.app_port,
            reload=True
        )

