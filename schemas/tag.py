from pydantic import BaseModel
from fastapi import Query

from typing import Annotated


class TagBody(BaseModel):
    title: Annotated[str, Query(max_length=50)]


class Tag(TagBody):
    id: int

    class Config:
        orm_mode = True