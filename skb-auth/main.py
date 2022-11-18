from services.api.service import APIService

api = APIService()


@api.app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

