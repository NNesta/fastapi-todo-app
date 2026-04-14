from pydantic import BaseModel, Field, EmailStr, ConfigDict
from uuid import UUID


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(min_length=1, max_length=120)
    first_name: str = Field(min_length=1, max_length=120)
    last_name: str = Field(min_length=1, max_length=120)


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class CreateUser(UserBase):
    password: str = Field(min_length=8, max_length=120)


class UserPrivate(BaseModel):
    email: EmailStr
