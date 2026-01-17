from fastapi import FastAPI
from pydantic import BaseModel

class Tasks(BaseModel):
    id: int
    title: str
    status: bool = False

app = FastAPI()
tasks = dict()
id_current = 1
@app.post("/tasks")        
def create_new_task(title: str, status: bool):
        global id_current
        create_task = {"id": id_current, "title": title, "status": status}
        tasks[id_current] = create_task
        id_current += 1
        return create_task
        
@app.get("/tasks")        
def read_task():
     return tasks
     
@app.get("/tasks/{id}")   
def update_id(id: int):
     if id in tasks:
         return tasks[id]
     else:
         return {"error": "Задача не найдена"}
         
@app.put("/tasks/{id}")
def update_status(id: int, status: bool):
     if id in tasks:
         tasks[id]["status"] = status
     else:
         return {"error": "Задача не найдена"}
     return tasks[id] 
     
@app.delete("/tasks/{id}")
def delete_tasks(id: int):
     if id in tasks:
         del tasks[id]
         return {"message": "Задача удалена"}
     else:
         return {"error": "Задача не найдена"}
         
     
     
 
 
        

