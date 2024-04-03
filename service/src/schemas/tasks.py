from datetime import datetime

from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    recieve_time: datetime
    write_time: datetime


class TaskSchemaAdd(BaseModel):
    id: int
    delay: int
