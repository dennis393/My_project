'''
import secrets
'''
from datetime import datetime, timedelta
from typing import Optional, Annotated
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv
import os
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from db_new import UserDB, get_db
from basemodel import TokenData

password_hash = PasswordHash.recommended()

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
LIVE_MINUTS_TOKEN = os.getenv("LIVE_MINUTS_TOKEN")
'''
print(secrets.token_hex(32))
'''

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Верификация пароля, возвращает хэштрованный пароль
def verify_password(plain_password: str, hashed_password: str):
     return password_hash.verify(plain_password, hashed_password)
 
#Хэширование пароля для сохранения в бд
def get_password_hash(password: str):
    return password_hash.hash(password)

#Создаем токен и его время жизни
def create_access_token(data: dict, time: Optional[timedelta] = None):
    to_encode = data.copy()
    if time:
        expire = datetime.utcnow() + time
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#верификация токена
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    return token_data

#Ищем пользователя в бд
def get_user(db, username:str):
     return db.query(UserDB).filter(UserDB.name == username).first()


#Текущий пользователь
def get_curr_user(token: Annotated[str, Depends(oauth2_scheme)], db = Depends(get_db)):
      credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось проверить учетные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
      token_data = verify_token(token, credentials_exception)
      user = get_user(db, token_data.username)
      if user is None:
           raise credentials_exception
      return user











