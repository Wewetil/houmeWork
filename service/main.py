import uvicorn
from fastapi import FastAPI

from src.api.routers import all_routers
from config import settings

HOST = settings.HOST
PORT = settings.PORT

app = FastAPI(title="User stories")

for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, host=HOST, port=PORT)
