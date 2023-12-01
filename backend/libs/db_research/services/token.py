import pydantic
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from libs.app.settings import get_settings
from libs.db_research.models import Token

settings = get_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_token_data(token: str = Depends(oauth2_scheme)):
    try:
        secret_key = settings.jwt_secret_key
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return Token(**payload)
    except (JWTError, pydantic.ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
