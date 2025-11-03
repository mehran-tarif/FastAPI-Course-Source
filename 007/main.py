from fastapi import FastAPI, status, HTTPException
from schemas import UserRequest, UserResponse, UserOutput
from typing import List

app = FastAPI()

users = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest):
    if any(u.email == user.email for u in users):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_user = UserOutput(
        id=len(users) + 1,
        **user.model_dump()
    )
    users.append(new_user)
    return {"message": "User created", "user": new_user}

@app.get("/user", response_model=List[UserOutput])
def get_users():
    return users