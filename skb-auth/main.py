from services.api.service import APIService
from database.service import init_db
import uvicorn

api = APIService()

if __name__ == '__main__':
    init_db()
    uvicorn.run("main:api.app", port=5000, reload=True, workers=1)
