from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def get_password_hash(password: str):
    return  password_hash.hash(password)