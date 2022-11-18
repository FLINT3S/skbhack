from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.get("/")
async def auth():
    return {"login": "processing 534"}

@auth_router.get("/healthcheck")
async def healthcheck():
    return {"healthcheck": "success"}
