import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker,DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI

class Base(DeclarativeBase):
    pass

#Асинхронное подключение к базе данных
async_engine = create_async_engine("postgresql+asyncpg://postgres:adminka69@localhost/asyncPost") #Создаем базу данных при помощи ассинхрона

#Асинхронная сессия
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

class Task(Base):
   __tablename__ = "Tasks" 
   id: Mapped[int] = mapped_column(primary_key=True)
   title: Mapped[str] = mapped_column(String(200))
   status: Mapped[bool] = mapped_column(default=False)

#Запуск ORM сервером
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


        
#Это запуск без сервера
async def main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
if __name__ == "__main__":
    asyncio.run(main())