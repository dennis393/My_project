from orm import Task, async_session
from fastapi import APIRouter, HTTPException
from sqlalchemy import select

router = APIRouter()

#Роутер для создания новой задачи
@router.post("/Task")
async def create_task(title: str, status: bool):
    async with async_session() as sess:
        try:
            newTask = Task(title = title, status = status)
            sess.add(newTask)
            await  sess.commit()
            return {"status_code": 200, "detail": "Задача создана"}
        except Exception:
            raise HTTPException(status_code=500, detail="Упс, что-то пошло не так, задача не создалась")

#Роутер для получения задачи
@router.get("/Task")
async def get_tasks():
    async with async_session() as sess:
        res = await sess.execute(select(Task)) #Выбираем базу данных
        return res.scalars().all() # Scalars() берет объекты из res, all() собирает в список

#Роутер для обновления статуса задачи
@router.put("/Task")
async def update_status(id:int, status:bool):
    async with async_session() as sess:
        res = await sess.execute(select(Task).where(Task.id == id)) #Выбираем поле id
        task = res.scalars().first() #Вытаскиваем объекты и берем только первый объект из результата
        if task is None:
            return "Задача не найдена"
        task.status = status
        await sess.commit()
        return f"{task.id}, {task.title}, {task.status}"

#Роутер для удаления задачи
@router.delete("/Task")
async def delete_task(id: int):
    async with async_session() as sess:
        get_task = await sess.execute(select(Task).where(Task.id == id))
        task = get_task.scalars().first()
        if task is None:
            return "Задача не найдена"
        sess.delete(task)
        result = f"Задача под номером {task.id} удалена"
        await sess.commit()
        return result
     