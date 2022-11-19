from services.api.service import APIService
from services.database.service import init_db
import uvicorn

api = APIService()


@api.app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == '__main__':
    init_db()
    uvicorn.run("main:api.app", port=5001, reload=True, workers=1)