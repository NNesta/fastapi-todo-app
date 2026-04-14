from typing import Any
from fastapi import APIRouter, status

from .service import delete_user, get_users, get_user
from .model import UserResponse, UserPrivate
from ..auth.service import DbSession, CurrentUser, get_current_user


router = APIRouter()


@router.get("/", response_model=list[UserResponse])
async def get_all_users(db: DbSession):
    return await get_users(db)


@router.get("/me", response_model=UserResponse)
async def current_user(current_user: CurrentUser):
    return current_user


@router.get("/{user_id}", response_model=UserResponse)
async def get_one_user(user_id: str, db: DbSession):
    return await get_user(user_id, db)


@router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None
)
async def delete(user_id: str, db: DbSession, current_user: CurrentUser):
    return await delete_user(user_id, current_user, db)
