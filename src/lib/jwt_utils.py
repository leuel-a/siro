from datetime import datetime, timezone, timedelta

from jose import jwt

from src.config.app_settings import settings


HASHING_ALGORITHM = "HS256"


def create_access_token(payload: dict, expires_delta: timedelta = timedelta(minutes=30)):
    """
    Generates a JWT access token.

    :param data: The data to be encoded in the token.
    :param expires_delta: The lifespan of the access token. Defaults to 30 minutes.

    :returns: The encoded JWT access token as a string.
    :rtype: str
    """
    to_encode = payload.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=HASHING_ALGORITHM)

