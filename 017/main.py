from fastapi import FastAPI, status, Depends
from schemas import UserRequest, UserResponse, UserOutput, UserPatchRequest
from typing import List
from services.user import UserService
from contextlib import asynccontextmanager
from dependencies import get_user_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.counter = 0
    app.state.user_service = UserService()
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    app.state.counter += 1
    print(f"Counter: {app.state.counter}")
    return {"Hello": "World", "counter": app.state.counter}

@app.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserRequest,
    user_service: UserService = Depends(get_user_service)
):
    new_user = user_service.create_user(user)
    return {"message": "User created", "user": new_user}

@app.get("/user", response_model=List[UserOutput])
def get_users(
    user_service: UserService = Depends(get_user_service),
):
    return user_service.get_users()

@app.get("/user/{user_id}", response_model=UserOutput)
def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
):
    return user_service.get_user(user_id)

@app.put("/user/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserRequest,
    user_service: UserService = Depends(get_user_service),
):
    existing_user = user_service.update_user(user_id, user)
    return {"message": "User updated", "user": existing_user}

@app.patch("/user/{user_id}", response_model=UserResponse)
def patch_user(
    user_id: int, user: UserPatchRequest,
    user_service: UserService = Depends(get_user_service),
):
    existing_user = user_service.patch_user(user_id, user)
    return {"message": "User updated", "user": existing_user}

@app.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
):
    user_service.delete_user(user_id)