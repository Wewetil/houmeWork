import time
from asyncio import Semaphore, create_task
from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import tasks_service
from src.schemas.tasks import TaskSchemaAdd
from src.services.tasks import TasksService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

semaphore = Semaphore(1)


@router.post("")
async def add_task(
    task: TaskSchemaAdd,
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
):
    try:
        recive_time = time.time()
        task_service = task.model_dump()
        task_service.update({"recive_time": recive_time})
        create_task(tasks_service.add_task(task_service, semaphore))

        return {"asyncAnswer": "ok"}
    except Exception as exc:
        return {"asyncAnswer": "error"}
