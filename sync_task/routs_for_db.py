from fastapi import APIRouter, HTTPException
from db_new import Task, UserDB, sessionlocal, get_db
from basemodel import newUser
from pwdlib import PasswordHash
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from secure import get_password_hash, verify_password, create_access_token, get_user, get_curr_user

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

@router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db = Depends(get_db)):
    user = get_user(db, form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    access_token = create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer"}



#Роутер для создания задачи, если пользователь зарегистрирован
@router.post("/Task")
def create_task(title: str, status: bool, current_user = Depends(get_curr_user)):
    data_base = sessionlocal()
    try:
        task1 = Task(title = title, status = status, user_id=current_user.id)
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

#Роутер обновления статуса задачи если пользователь аутентифицирован, конкретный пользователь
#Может изменить статус только у своей задачи
@router.put("/Task")      
def update_status(id: int, status: bool, current_user = Depends(get_curr_user)):
    data_base = sessionlocal() 
    task = data_base.get(Task, id)
    if task is None:
        return "Задача не найдена"
    if task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Нет доступа")
    task.status = status
    res =  f"{task.id}, {task.title}, {task.status}"
    data_base.commit()
    data_base.close()
    return res

#Роутер удаления задачи если пользователь аутентифицирован, конкретный пользователь
#Может удалить только свою задачу  
@router.delete("/Task")    
def delete_task(id: int, current_user = Depends(get_curr_user)):
    data_base = sessionlocal()
    task_for_del = data_base.get(Task, id)
    if task_for_del is None:
        return "Задача не найдена"
    
    if task.user_id != current_user.id:
        raise HTTPexception(status_code=403, detail="Нет доступа")
    data_base.delete(task_for_del)
    result = f"Задача под номером {task_for_del.id} удалена"
    data_base.commit()
    data_base.close()
    return result