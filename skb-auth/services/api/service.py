from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import auth_router, admin_router


class APIService:
    def __init__(self):
        self.debug = True
        self.app = FastAPI(
            title="API",
        )

        #TODO убрать *
        origins = ["*"]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=[""],
            allow_headers=[""],
        )


        self.attach_routes()

    def attach_routes(self):
        api_router = APIRouter()
        api_router.prefix = "/api"

        api_router.include_router(router=admin_router, prefix="/admin", tags=["Admin"])
        api_router.include_router(router=auth_router, prefix="/auth", tags=["Auth"])
        self.app.include_router(router=api_router)
