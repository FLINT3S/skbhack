from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from starlette import status

from ...database.service import get_session
from ...database.models import User, Role

from .dtos import *

admin_router = APIRouter()


#  @admin_required
@admin_router.get("/not_verified_users")
async def not_verified_users(
        session: Session = Depends(get_session)
):
    return session.exec(select(User).where(User.verify == False)).all()


#  @admin_required
@admin_router.get("/verified_users")
async def verified_users(
        session: Session = Depends(get_session)
):
    return session.exec(select(User).where(User.verify)).all()


#  @admin_required
@admin_router.post("/verify_user")
async def verify_user(
        login_dto: LoginDto,
        session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.login == login_dto.login)).first()
    user.verify = True

    session.add(user)
    session.commit()
    return status.HTTP_200_OK


@admin_router.post("/dismiss_user")
async def verify_user(
        login_dto: LoginDto,
        session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.login == login_dto.login)).first()

    session.delete(user)
    session.commit()

    return status.HTTP_200_OK


#  @admin_required
@admin_router.post("/block_user")
async def block_user(
        login_dto: LoginDto,
        session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.login == login_dto.login)).first()

    if user.firstname != "admin":
        user.blocked = True

        session.add(user)
        session.commit()
        
    return status.HTTP_200_OK


#  @admin_required
@admin_router.post("/unblock_user")
async def unblock_user(
        login_dto: LoginDto,
        session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.login == login_dto.login)).first()
    user.blocked = False

    session.add(user)
    session.commit()
    return status.HTTP_200_OK


#  @admin_required
@admin_router.post("/change_role")
async def change_role(
        role_dto: RoleChangeDto,
        session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.login == role_dto.login)).first()
    user.role = session.exec(select(Role).where(Role.name == role_dto.role_name)).first()

    session.add(user)
    session.commit()
    return status.HTTP_200_OK
