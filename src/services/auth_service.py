from sqlalchemy import select

from src.models import User
from src.lib.db import SessionDep
from src.lib.app_error import AppError, AppEnum
from src.lib.utils import check_password
from src.models.auth import AuthLoginRequest


def login_user(user: AuthLoginRequest, session: SessionDep):
    """
    Login a user by checking the password

    :param user: The credential user login information
    :param session: The database session dependecy
    """
    statement = select(User).where(User.email == user.email)
    result: User | None = session.exec(statement).scalar_one_or_none()

    if not result:
        raise AppError(AppEnum.INVALID_EMAIL_OR_PASSWORD, 'Invalid Email or Password')

    password_match = check_password(user.password, result.password)
    if not password_match:
        raise AppError(AppEnum.INVALID_EMAIL_OR_PASSWORD, 'Invalid Email or Password')
    return result

