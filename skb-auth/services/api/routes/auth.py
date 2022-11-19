import jwt
import os

from ...database.service import get_session
from ...database.models import User, Account, Currency

from dotenv import load_dotenv

from fastapi import APIRouter, Depends

from sqlmodel import Session, select

from starlette import status
from starlette.responses import Response

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
    user = User.get_instance(
        login=create_user_dto.login,
        firstname=create_user_dto.firstname,
        surname=create_user_dto.surname,
        password=create_user_dto.password
    )

    currency = session.exec(select(Currency).where(Currency.ticker == "RUB")).first()
    account = Account.get_instance(user, currency)

    session.add(account)
    session.add(user)
    session.commit()
    return jwt.encode(user, secret_key, algorithm="HS256")


@auth_router.post("/login")
async def login(
        login_user_dto: LoginUserDto,
        session: Session = Depends(get_session)
):
    user_login = login_user_dto.login
    user = session.exec(select(User).where(User.login == user_login)).first()
    if user is None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    # Create and return jwt token
    if user.check_password(str(login_user_dto.password)):
        return jwt.encode(user, secret_key, algorithm="HS256")
    return status.HTTP_400_BAD_REQUEST


@auth_router.post("/change_password")
async def change_password(
        login_user_dto: LoginUserDto,
        session: Session = Depends(get_session)
):
    user_login = login_user_dto.login
    user = session.exec(select(User).where(User.login == user_login)).first()
    if user is None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    if user.check_password(login_user_dto.password):
        user.set_password(login_user_dto.password)
    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
