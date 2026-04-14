from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .model import Token
from ..user.model import UserResponse, CreateUser
from src.database.core import DbSession
from typing import Annotated
from .service import create_user, token


router = APIRouter()


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def register(user: CreateUser, db: DbSession):
    return await create_user(user, db)


@router.post("/login", response_model=Token)
async def login(
    login_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: DbSession
):
    return await token(
        username=login_data.username, password=login_data.password, db=db
    )
