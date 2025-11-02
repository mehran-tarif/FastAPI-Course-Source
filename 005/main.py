from cgitb import reset
from fastapi import FastAPI
from schemas import UserRequest, UserResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user", response_model=UserResponse)
def create_user(user: UserRequest):
    return {"message": "User created", "user": user}