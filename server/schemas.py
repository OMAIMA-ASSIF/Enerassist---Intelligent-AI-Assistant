from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6)

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr

    class Config:
        # Pydantic v2 usage might differ slightly, but this is generally safe for v1/v2 compat or v1
        pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
