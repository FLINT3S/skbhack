from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import balance_router, index_router


class APIService:
    def __init__(self):
        self.debug = True
        self.app = FastAPI(
            title="API",
        )

        self.app.add_middleware(
            CORSMiddleware,
            allow_credentials=True,
            allow_methods=[""],
            allow_headers=[""],
        )

        self.attach_routes()

    def attach_routes(self):
        api_router = APIRouter()
        api_router.prefix = "/api"

        api_router.include_router(router=balance_router, prefix="/balance", tags=["Balance"])
        api_router.include_router(router=index_router, prefix="/index", tags=["Index"])
        self.app.include_router(router=api_router)
