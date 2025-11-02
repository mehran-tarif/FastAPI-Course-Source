from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user/{user_name:str}/{age:int}")
def hello_user(user_name: str, age: int):
    return {"user_name": user_name, "age": age}

@app.get("/admin")
def hello_admin(user_name: str = None, age: int = None):
    return {"user_name": user_name, "age": age}