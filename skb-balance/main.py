from api.service import APIService
from database.service import test
import uvicorn

api = APIService()

test()

@api.app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == '__main__':
    uvicorn.run("main:api.app", port=5001, reload=True, workers=1)