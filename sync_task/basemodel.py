from pydantic import BaseModel
from datetime import datetime
#Модель для нового пользователя
class newUser(BaseModel):
    username: str
    userpassword: str
 
#Схема для JWT токена, аутентификация  
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

#Для задач
class Tasks(BaseModel):
    id: int | None = None
    title: str | None = None
    status: bool = False