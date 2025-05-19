from fastapi import FastAPI
import uvicorn

from src.config import settings


app = FastAPI()


@app.get("/")
def home_api() -> dict:
    return {"message": "add docs to link"}


@app.get("/DB.URL")
def db_url() -> dict:
    return {"DB url": settings.db_url}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
