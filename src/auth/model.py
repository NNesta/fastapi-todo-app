from uuid import UUID
from pydantic import BaseModel, EmailStr, SecretStr, Field, ConfigDict
from ..user.model import UserBase


class RegisterUserRequest(UserBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str | None = None

    def get_uuid(self) -> UUID | None:
        if self.user_id:
            return UUID(self.user_id)
        return None


class Credential(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8, max_length=120)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(min_length=1, max_length=120)
    first_name: str = Field(min_length=1, max_length=120)
    last_name: str = Field(min_length=1, max_length=120)
    password_hash: SecretStr = Field(min_length=8, max_length=120)
