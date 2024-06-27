from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from typing import Annotated
from fastapi import Query


class Status(str, Enum):
    active = "active"
    blocked = "blocked"
    deleted = "deleted"


class AuthorBody(BaseModel):
    nickname: Annotated[str, Query(max_length=50)]
    email: Annotated[str, Query(max_length=200)]
    password: str # password hash
    status: Status


class Author(AuthorBody):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True