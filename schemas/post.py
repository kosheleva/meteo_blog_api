from pydantic import BaseModel
from fastapi import Query

from typing import Annotated
from datetime import datetime

from .author import Author
from .tag import Tag
from .category import Category


class PostBody(BaseModel):
    author_id: int
    category_id: int
    title: Annotated[str, Query(max_length=300)]
    content: str
    is_visible: bool


class Post(PostBody):
    id: int
    author: Author
    category: Category
    tags: list[Tag]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True