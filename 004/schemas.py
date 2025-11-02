from pydantic import BaseModel, Field, EmailStr

class UserRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="The name of the user")
    age: int = Field(..., ge=1, le=120, description="The age of the user")
    email: EmailStr = Field(..., format="email", description="The email of the user")
    password: str = Field(..., min_length=8, max_length=100, description="The password of the user")