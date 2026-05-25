from pydantic import BaseModel
from datetime import datetime

class newUser(BaseModel):
    username: str
    userpassword: str
    

class Tasks(BaseModel):
    id: int | None = None
    title: str | None = None
    status: bool = False