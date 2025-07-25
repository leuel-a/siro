#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv


load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from typing import Dict
from contextlib import asynccontextmanager

import uvicorn
from sqlmodel import select
from fastapi import FastAPI, HTTPException

from src.lib.db import init_db, SessionDep
from src.routes import user_router, auth_router
from src.config.app_settings import settings


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

API_PREFIX = '/api'

app.include_router(auth_router.router, prefix=f"{API_PREFIX}/auth", tags=["Auth"])
app.include_router(user_router.router, prefix=f"{API_PREFIX}/users", tags=["Users"])


if __name__ == "__main__":
    uvicorn.run(
            "main:app",
            host=settings.app_host,
            port=settings.app_port,
            reload=True
        )

