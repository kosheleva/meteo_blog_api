from fastapi import APIRouter, Depends, HTTPException
from db import get_db, get_all, get_by_id, create, update, delete

from models.tag import Tag as TagModel
from schemas.tag import TagBody, Tag


router = APIRouter(
    prefix="/tags",
    tags=["tags"],
    dependencies=[Depends(get_db)]
)


@router.get("/")
async def get_tags(offset: int = 0, limit: int = 100, response_model=list[Tag]):
    db = next(router.dependencies[0].dependency())

    return get_all(db, TagModel, offset, limit)


@router.get("/{tag_id}")
async def get_tag(tag_id: str, response_model=Tag):
    db = next(router.dependencies[0].dependency())

    tag = get_by_id(db, TagModel, tag_id)

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    return tag


@router.post("/")
async def create_tag(tag: TagBody, response_model=Tag):
    db = next(router.dependencies[0].dependency())

    new_tag = TagModel(
        title = tag.title
    )

    return create(db, new_tag)


@router.put("/{tag_id}")
async def update_tag(tag_id: str, tag: TagBody, response_model=Tag):
    db = next(router.dependencies[0].dependency())

    existed_tag = get_by_id(db, TagModel, tag_id)

    if not existed_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    return update(db, existed_tag, tag)


@router.delete("/{tag_id}")
async def delete_tag(tag_id: str, response_model=bool):
    db = next(router.dependencies[0].dependency())

    return delete(db, TagModel, tag_id)