from fastapi import FastAPI

app = FastAPI()

@app.get("/item")
def read_item():
    return {"message": "Hello world"}