from starlette.middleware.cors import CORSMiddleware

from services.api.service import APIService
from services.database.service import init_db
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
    init_db()
    uvicorn.run("main:api.app", port=5000, reload=True, workers=1)
