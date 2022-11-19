from fastapi import APIRouter

buy_router = APIRouter()

@buy_router.get("/")
async def index():
    return {"status": "OK!!"}