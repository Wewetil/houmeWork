import os
import aiofiles
from abc import ABC, abstractmethod

import aiofiles


class AbstractRepository(ABC):
    @abstractmethod
    async def add():
        raise NotImplementedError


class FileSystemRepository(AbstractRepository):

    async def add(self, task: dict, file_name: str):
        path = f"{os.getcwd()}/files/"
        file_path = f"{path}{file_name}.txt"
        async with aiofiles.open(file_path, "w") as file:
            await file.write(str(task))
