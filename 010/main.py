from fastapi import FastAPI, status, HTTPException
from schemas import UserRequest, UserResponse, UserOutput, UserPatchRequest
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
    existing_user = next((u for u in users if u.id == user_id), None)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return existing_user

@app.put("/user/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserRequest):
    existing_user = next((u for u in users if u.id == user_id), None)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if any(u.email == user.email and u.email != existing_user.email for u in users):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    for key, value in user.model_dump().items():
        if hasattr(existing_user, key):
            setattr(existing_user, key, value)

    return {"message": "User updated", "user": existing_user}

@app.patch("/user/{user_id}", response_model=UserResponse)
def patch_user(user_id: int, user: UserPatchRequest):
    existing_user = next((u for u in users if u.id == user_id), None)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if any(u.email == user.email and u.email != existing_user.email for u in users):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    for key, value in user.model_dump().items():
        if hasattr(existing_user, key) and value is not None:
            setattr(existing_user, key, value)

    return {"message": "User updated", "user": existing_user}

@app.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    existing_user = next((u for u in users if u.id == user_id), None)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    users.remove(existing_user)