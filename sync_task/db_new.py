from sqlalchemy import create_engine, MetaData, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped, mapped_column
from dotenv import load_dotenv
import os
import psycopg2


class Base(DeclarativeBase):
    pass

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)

class UserDB(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    hashed_password: Mapped[str] 
 


class Task(Base):
    __tablename__ = 'Taskes'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    status: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"), nullable=True)
    

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

sessionlocal = sessionmaker(bind=engine)