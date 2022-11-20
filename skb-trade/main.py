from services.api.service import APIService
import uvicorn

api = APIService()

if __name__ == '__main__':
    uvicorn.run("main:api.app", port=5002, reload=True, workers=1)
