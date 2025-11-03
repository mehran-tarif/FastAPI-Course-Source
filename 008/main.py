from fastapi import FastAPI, status, HTTPException
from schemas import UserRequest, UserResponse, UserOutput
from typing import List
from pydantic import EmailStr

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

@app.get("/user/{user_id}", response_model=UserOutput)
def get_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

# @app.get("/user/email/{email}", response_model=UserOutput)
# def get_user_by_email(email: EmailStr):
#     user = next((u for u in users if u.email == email), None)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     return user