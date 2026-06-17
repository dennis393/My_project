from fastapi import FastAPI
from Basemodel import Tasks
from orm import Base, Task
from routs import router
from orm import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(router)

@app.get("/")
async def main():
    return {"Этот  менеджер задач работает по асинхронному методу программирования"}