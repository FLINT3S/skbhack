from fastapi import APIRouter, Depends, Form
from sqlmodel import Session, select

from ...database.service import get_session
from ...database.models import User, Role, Account, Currency

from .dtos import CreateUserDto

auth_router = APIRouter()


@auth_router.post("/register")
async def register(
        create_user_dto: CreateUserDto,
        session: Session = Depends(get_session)
):
    user = User.get_instance(
        firstname=create_user_dto.firstname,
        surname=create_user_dto.surname,
        password=create_user_dto.password
    )

    currency = session.exec(select(Currency).where(Currency.ticker == "RUB")).first()
    account = Account.get_instance(user, currency)

    session.add(account)
    session.add(user)
    session.commit()
    return user
