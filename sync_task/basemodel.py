from pydantic import BaseModel
from datetime import datetime

class newUser(BaseModel):
    username: str
    userpassword: str
 
#Схема для JWT токена, аутентификация  
class Token(BaseModel):
    access_token: str
    token_type: str


class Tasks(BaseModel):
    id: int | None = None
    title: str | None = None
    status: bool = False