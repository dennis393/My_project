from fastapi import APIRouter, HTTPException
from db_new import Task, sessionlocal, UserDB
from basemodel import newUser
from pwdlib import PasswordHash
from secure import get_password_hash

router = APIRouter()

#Создаем нового пользователя, роут принимает Pydantic модель
@router.post("/register")
def create_new_user(new_user: newUser):
    data_base = sessionlocal()
    user = data_base.query(UserDB).filter(UserDB.name == new_user.username).first()
    #Если пользователь уже зарегистрирован
    if user:
         raise HTTPException(
            status_code=400,
            detail="Пользователь уже зарегистрирован"
        )
    #Хэшируем пароль
    hashed_password = get_password_hash(new_user.userpassword)
    
    #Pydantic модель нельзя добавить в бд, создаем ORM объект
    user_db = UserDB(name=new_user.username, hashed_password=hashed_password)
    
    #добавляем пользователя в бд
    data_base.add(user_db)
    data_base.commit()
    data_base.close()
    
    return "Пользователь успешно добавлен"


#Тут будет роутер с аутентификацией
@router.post("/Authentication")


@router.post("/Task")
def create_task(title: str, status: bool):
    data_base = sessionlocal()
    try:
        task1 = Task(title = title, status = status)
        data_base.add(task1)
        data_base.commit()
        data_base.close()
        return "Задача создана"
    except Exception as e:
        print(f"Ошибка {e}")
        data_base.close()
        raise HTTPException(status_code=500,detail = "Упс, что-то пошло не так, задача не создалась")
       

@router.get("/Task")     
def get_list_tasks():
        data_base = sessionlocal()
        tasks = data_base.query(Task).all()
        data_base.close()
        return tasks


@router.put("/Task")      
def update_status(id: int, status: bool):
    data_base = sessionlocal() 
    task = data_base.get(Task, id)
    if task is None:
        return "Задача не найдена"
    task.status = status
    res =  f"{task.id}, {task.title}, {task.status}"
    data_base.commit()
    data_base.close()
    return res
    
@router.delete("/Task")    
def delete_task(id: int):
    data_base = sessionlocal()
    task_for_del = data_base.get(Task, id)
    if task_for_del is None:
        return "Задача не найдена"
    data_base.delete(task_for_del)
    result = f"Задача под номером {task_for_del.id} удалена"
    data_base.commit()
    data_base.close()
    return result