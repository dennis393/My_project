from typing import Annotated
from fastapi import FastAPI, Depends
from basemodel import Tasks
from db_new import Base, Task
from routs_for_db import router
from secure import oauth2_scheme

app = FastAPI()
app.include_router(router)

@app.get("/auth")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

def main_func():
    return {"Добро пожаловать в приложение"}