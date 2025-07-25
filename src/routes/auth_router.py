from fastapi import APIRouter, HTTPException

from src.lib.db import SessionDep
from src.config.http_status import HTTPStatus
from src.lib.app_error import AppError
from src.lib.jwt_utils import create_access_token
from src.services.auth_service import login_user
from src.models.auth import AuthLoginRequest, AuthLoginResponse

router = APIRouter()


@router.post('/login', response_model=AuthLoginResponse)
async def login_users(user: AuthLoginRequest, session: SessionDep):
    """Login a user based on their credentials"""

    try:
        user_from_db = login_user(user, session)

        payload = { "id": user_from_db.id, "email": user_from_db.email}
        access_token = create_access_token(payload)
        return {"access_token": access_token, "id": user_from_db.id}

    except AppError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=e.message)



