from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="The name of the user")
    age: int = Field(..., ge=1, le=120, description="The age of the user")
    email: EmailStr = Field(..., format="email", description="The email of the user")
    password: str = Field(..., min_length=8, max_length=100, description="The password of the user")


class UserPatchRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50, description="The name of the user")
    age: Optional[int] = Field(None, ge=1, le=120, description="The age of the user")
    email: Optional[EmailStr] = Field(None, format="email", description="The email of the user")
    password: Optional[str] = Field(None, min_length=8, max_length=100, description="The password of the user")


class UserOutput(BaseModel):
    id: int = Field(..., description="The id of the user")
    name: str = Field(..., min_length=3, max_length=50, description="The name of the user")
    age: int = Field(..., ge=1, le=120, description="The age of the user")
    email: EmailStr = Field(..., format="email", description="The email of the user")


class UserResponse(BaseModel):
    message: str = Field(..., description="The message of the response")
    user: UserOutput = Field(..., description="The user of the response")