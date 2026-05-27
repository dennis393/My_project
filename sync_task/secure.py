'''
import secrets
'''
from dotenv import load_dotenv
import os
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError

password_hash = PasswordHash.recommended()

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
LIVE_MINUTS_TOKEN = os.getenv("LIVE_MINUTS_TOKEN")
'''
print(secrets.token_hex(32))
'''

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Хэширование пароля
def get_password_hash(password: str):
    return password_hash.hash(password)







