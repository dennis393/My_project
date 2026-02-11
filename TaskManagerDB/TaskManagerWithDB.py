import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

class Tasks(BaseModel):
    id: int
    description: str
    status: bool = False

app = FastAPI()

connection = sqlite3.connect('data_base.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Tasks(
id INTEGER PRIMARY KEY,
description TEXT NOT NULL,
status INTEGER DEFAULT 0)
''')
connection.commit()


@app.post("/tasks")
def create_new_task(description: str, status: bool = False):    
    connection = sqlite3.connect('data_base.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Tasks( description, status) VALUES(?, ?)',(description, status))
    connection.commit() #сначало сохраняем
    tasks_id = cursor.lastrowid #вытаскиваем id
    cursor.close() #затем закрываем
    connection.close()
    return {
    "id":tasks_id,
    "description": description,
    "status": bool(status)
    }


@app.get("/tasks")
def get_all_tasks():
    connection = sqlite3.connect('data_base.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Tasks')
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    return tasks


@app.get("/tasks/{id}")    
def get_one_task(id: int):
    connection = sqlite3.connect('data_base.db')
    cursor = connection.cursor()
    cursor.execute('SELECT *  FROM Tasks WHERE id = ?', (id,))
    task = cursor.fetchone()
    cursor.close()
    connection.close()
    if task is None:
        return {"error": "Задача не найдена"}
    else:
        return {"id": task[0],
                     "description": task[1],
                     "status": bool(task[2])
        }

                
@app.put("/tasks/{id}")   
def update_status(id: int, status: bool):
    connection = sqlite3.connect('data_base.db')    
    cursor = connection.cursor() 
    cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, id))
    connection.commit()
    answer = cursor.rowcount #колличество измененных строк
    cursor.close()
    connection.close()
    if answer == 0: #если 0, значит ничего не обновилось задачи такой неи
        return {"error": "Задача не найдена"}
    else:
        return {"id": id, "status": bool(status)}

        
@app.delete("/tasks/{id}")   
def delete_task(id: int):
    connection = sqlite3.connect('data_base.db')        
    cursor = connection.cursor() 
    cursor.execute('DELETE FROM Tasks WHERE id = ?',(id,))
    connection.commit()
    answer = cursor.rowcount
    cursor.close()
    connection.close()
    if answer == 0:
        return {"error": "Задача не найдена"}
    else:
        return {"message": "Задача удалена"}
        
