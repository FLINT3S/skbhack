from uuid import UUID

import jwt
import os

from starlette.responses import JSONResponse, Response

from ...database.service import get_session
from ...database.models import User, Account, Currency

from dotenv import load_dotenv

from fastapi import APIRouter, Depends, HTTPException

from sqlmodel import Session, select

from starlette import status

from .dtos import *


load_dotenv()
secret_key = os.environ["SECRET_KEY"]

auth_router = APIRouter()


# For docker
@auth_router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@auth_router.post("/register")
async def register(
        create_user_dto: CreateUserDto,
        session: Session = Depends(get_session)
):
    if session.exec(select(User).where(User.login == create_user_dto.login)).first() is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Такой логин уже есть в базе.")

    user = User.get_instance(
        login=create_user_dto.login,
        firstname=create_user_dto.firstname,
        surname=create_user_dto.surname,
        password=create_user_dto.password
    )

    currency = session.exec(select(Currency).where(Currency.ticker == "RUB")).first()
    account = Account.get_instance(user, currency)
    account.amount = 10_000

    session.add(account)
    session.add(user)
    session.commit()
    user.id = str(user.id)
    return jwt.encode(user.dict(), secret_key, algorithm="HS256")


@auth_router.post("/login")
async def login(
        login_user_dto: LoginUserDto,
        session: Session = Depends(get_session)
):
    user_login = login_user_dto.login
    user = session.exec(select(User).where(User.login == user_login)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Такого пользователя не существует.")
    if user.blocked:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Blocked.")
    if not user.verify:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Unverified.")

    # Create and return jwt token
    user.id = str(user.id)
    if user.check_password(str(login_user_dto.password)):
        return jwt.encode(user.dict(), secret_key, algorithm="HS256")

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Пароли не совпадают.")


@auth_router.post("/change_password")
async def change_password(
        login_user_dto: LoginUserDto,
        session: Session = Depends(get_session)
):
    user_login = login_user_dto.login
    user = session.exec(select(User).where(User.login == user_login)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Такого пользователя не существует.")

    if user.check_password(str(login_user_dto.password)):
        user.set_password(str(login_user_dto.password))
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Пароли не совпадают.")


@auth_router.get("/getUser/{user_id}")
async def get_user_info(user_id: UUID, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content={
        "id": str(user.id),
        "firstname": user.firstname,
        "surname": user.surname,
        "login": user.login,
        "blocked": user.blocked,
        "verified": user.verify
    })
