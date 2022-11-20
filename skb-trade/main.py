from starlette.middleware.cors import CORSMiddleware

from services.api.service import APIService
import uvicorn

api = APIService()

api.app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("main:api.app", port=5002, reload=True, workers=1)
