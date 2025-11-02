from fastapi import FastAPI
from schemas import UserRequest

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user")
def create_user(user: UserRequest):
    return {"message": "User created", "user": user}