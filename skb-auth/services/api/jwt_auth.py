import jwt
import os

from fastapi import HTTPException
from functools import wraps
from dotenv import load_dotenv
from starlette import status

load_dotenv()
secret_key = os.environ["SECRET_KEY"]


def auth_required(func):
    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        jwt_key = request.headers["Authorization"].strip()

        if jwt.decode(jwt_key, secret_key, algorithms=["HS256"])["role"] not in ["User"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Нет доступа.")

        return await func(request, *args, **kwargs)

    return wrapper


def admin_required(func):
    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        jwt_key = request.headers["Authorization"].strip()

        if jwt.decode(jwt_key, secret_key, algorithms=["HS256"])["role"] not in ["Admin"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Нет доступа.")

        return await func(request, *args, **kwargs)

    return wrapper