from re import S
from fastapi import APIRouter, status

from src.database.core import DbSession
from src.task.service import create_task
from .model import CreateTask, TaskResponse, UpdateData
from ..auth.service import CurrentUser
from .service import get_tasks, get_task, delete_task, update_task
from typing import List


router = APIRouter()


@router.get("/{task_id}", response_model=TaskResponse)
async def get_one(task_id: str, current_user: CurrentUser, db: DbSession):
    return await get_task(task_id, current_user, db)


@router.get("/", response_model=List[TaskResponse])
async def get_all(db: DbSession):
    return await get_tasks(db)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create(task_data: CreateTask, current_user: CurrentUser, db: DbSession):
    return await create_task(task_data, current_user, db)


@router.patch("/{task_id}", response_model=TaskResponse)
async def update(
    task_id: str, current_user: CurrentUser, task_data: UpdateData, db: DbSession
):
    return await update_task(task_id, current_user, task_data, db)


@router.delete("/{task_id}", response_model=None)
async def delete(task_id: str, current_user: CurrentUser, db: DbSession):
    return await delete_task(task_id, current_user, db)
