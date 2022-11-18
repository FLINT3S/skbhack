from fastapi import APIRouter, FastAPI

from . import routes


class APIService:
    def __init__(self):
        self.debug = True
        self.app = FastAPI(
            title="API",
        )

        self.attach_routes()

    def attach_routes(self):
        api_router = APIRouter()
        api_router.prefix = "/api"

        api_router.include_router(router=routes.auth_router, prefix="/auth", tags=["Auth"])
        api_router.include_router(router=routes.index_router, prefix="/index", tags=["Index"])
        self.app.include_router(router=api_router)
