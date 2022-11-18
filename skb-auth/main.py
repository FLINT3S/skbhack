from services.api.service import APIService
from services.database.service import test

api = APIService()

test()

@api.app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
