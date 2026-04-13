from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from ..entities import Priority

from src.user.model import UserBase


class TaskBase(BaseModel):
    title: str = Field(min_length=10, max_length=200)
    description: str = Field(min_length=10)
    due_date: datetime = Field(default_factory=datetime.now)


class CreateTask(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: UUID
    completed_at: datetime | None = None
    is_complete: bool | None = Field(default=False)
    priority: Priority = Priority.MEDIUM


class UpdateData(BaseModel):
    title: str | None = Field(default=None, min_length=10, max_length=200)
    description: str | None = Field(default=None, min_length=10)
    due_date: datetime | None = Field(default=None)
    completed_at: datetime | None = Field(default=None)
    is_complete: bool | None = Field(default=None)
    priority: Priority | None = Priority.MEDIUM
