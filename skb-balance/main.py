from services.api.service import APIService
import uvicorn

api = APIService()


@api.app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == '__main__':
    uvicorn.run("main:api.app", port=5001, reload=True, workers=1)