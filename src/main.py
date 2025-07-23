#!/usr/bin/env python3
import uvicorn
from dotenv import load_dotenv
from typing import Annotated, List
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Session, create_engine, text, select

from src.db import init_db
from src.models import User
from config.app_settings import settings

load_dotenv()

app = FastAPI()

SessionDep = Annotated[Session, Depends(get_session)] ## this is to type the session


@app.on_event('startup')
    def on_startup():
        init_db()


@app.get('/checkhealth')
async def checkhealth(session: SessionDep):
    try:
        session.exec(text("SELECT 1"))
        return {'db': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")


@app.get("/users/", response_model=List[User])
def read_users(session: SessionDep):
    """
    Retrieves all users from the database.
    """
    users = session.exec(select(User)).all()
    return users


if __name__ == "__main__":
    uvicorn.run(
            "main:app",
            host=settings.app_host,
            port=settings.app_port,
            reload=True
        )

