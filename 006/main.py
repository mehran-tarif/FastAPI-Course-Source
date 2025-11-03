from fastapi import FastAPI, status
from schemas import UserRequest, UserResponse, UserOutput

app = FastAPI()

users = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest):
    # print(user.model_dump())
    new_user = UserOutput(
        id=len(users) + 1,
        **user.model_dump()
    )
    users.append(new_user)
    return {"message": "User created", "user": new_user}