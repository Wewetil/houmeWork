import asyncio
import time

from src.utils.repository import AbstractRepository


class TasksService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def add_task(self, task: dict, semaphore):
        await semaphore.acquire()
        resp = await self.tasks_repo.add(task, f"{str(task.get('recive_time'))}_{task.get('id')}")
        await asyncio.sleep(task.get("delay"))
        task.update({"write_time": time.time()})
        resp = await self.tasks_repo.add(task, f"{str(task.get('write_time'))}_{task.get('id')}")
        semaphore.release()
