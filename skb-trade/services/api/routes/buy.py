from fastapi import APIRouter, Depends
from sqlmodel import Session

from ...database.service import get_session

buy_router = APIRouter()

@buy_router.get("/")
async def buy(session: Session = Depends(get_session)):
    return session