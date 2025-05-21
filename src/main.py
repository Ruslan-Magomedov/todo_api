from fastapi import FastAPI
import uvicorn

from src.routers.todo import router as todo_router


app = FastAPI()
app.include_router(todo_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
