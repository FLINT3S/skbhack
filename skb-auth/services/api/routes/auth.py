from fastapi import APIRouter, Depends, Form
from sqlmodel import Session

from ...database.service import get_session
from ...database.models import User, Role, Account

auth_router = APIRouter()


@auth_router.get("/register")
async def register(
        session: Session = Depends(get_session)
):
    user = User.get_instance(
        firstname="Filipp",
        surname="Zakharov",
        password="1" * 60
    )
    session.add(user)
    session.commit()
    return {"login": "processing 123"}
