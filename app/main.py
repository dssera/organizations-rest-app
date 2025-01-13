import uvicorn
from fastapi import FastAPI, Depends

from app.dependencies import verify_api_key
from .api.api_v1.endpoints import organizations


app = FastAPI()
app.include_router(organizations.router, dependencies=[Depends(verify_api_key)], tags=["Organizations"])


if __name__ == '__main__':
    uvicorn.run(host="localhost", port=80, app="main:app", reload=True)


