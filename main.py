from fastapi import FastAPI
from basemodel import Tasks
from db_new import Base, Task
from routs_for_db import router

app = FastAPI()
app.include_router(router)

def main_func():
    return {"Добро пожаловать в приложение"}