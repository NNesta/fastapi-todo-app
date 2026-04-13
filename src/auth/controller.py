from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .model import Token, RegisterUserRequest, Credential, UserResponse
from src.database.core import DbSession
from typing import Annotated
from .service import token, delete_user, create_user, get_users, get_user, CurrentUser
from ..entities import User


router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: RegisterUserRequest, db: DbSession):
    return await create_user(user, db)


@router.post("/login", response_model=Token)
async def login(
    login_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: DbSession
):
    return await token(
        username=login_data.username, password=login_data.password, db=db
    )


@router.get("/", response_model=list[UserResponse])
async def get_all_users(db: DbSession):
    return await get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
async def get_one_user(user_id: str, db: DbSession):
    return await get_user(user_id, db)


@router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None
)
async def delete(user_id: str, db: DbSession, current_user: CurrentUser):
    return await delete_user(user_id, current_user, db)
