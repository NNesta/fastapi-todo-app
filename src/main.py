from fastapi import FastAPI
from . import entities
from .auth import router as auth_router
from .task import router as task_router
from .user import router as user_router


app = FastAPI(title="Todo app")
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(task_router, prefix="/api/task", tags=["task"])
app.include_router(user_router, prefix="/api/user", tags=["user"])
