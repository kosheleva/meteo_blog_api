from pydantic import BaseModel
from typing import Annotated
from fastapi import Query


class CategoryBody(BaseModel):
    title: Annotated[str, Query(max_length=100)]


class Category(CategoryBody):
    id: int

    class Config:
        orm_mode = True
    

