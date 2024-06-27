from fastapi import APIRouter, Depends, HTTPException

from db import get_db, get_all, get_by_id, get_by_ids, create, update, delete

from models.post import Post as PostModel
from models.tag import Tag as TagModel
from schemas.post import PostBody, Post


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    dependencies=[Depends(get_db)]
)


@router.get("/")
async def get_posts(offset: int = 0, limit: int = 100) -> list[Post]:
    db = next(router.dependencies[0].dependency())

    return get_all(db, PostModel, offset, limit)


@router.get("/{post_id}")
async def get_post(post_id: int) -> Post:
    db = next(router.dependencies[0].dependency())

    post = get_by_id(db, PostModel, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.post("/")
async def create_post(post: PostBody, tags: list[int], response_model=Post):
    db = next(router.dependencies[0].dependency())

    new_post = PostModel(
        # usually author_id should be taken from access token,
        # for this project just send it in request
        author_id = post.author_id, 
        category_id = post.category_id,
        title = post.title,
        content = post.content,
        is_visible = post.is_visible
    )

    created_post = create(db, new_post)

    # let's assume, that user on client side can assign tags
    # to post from the list of existing tags,
    # so just append them to post
    existed_tags = get_by_ids(db, TagModel, tags)

    for tag in existed_tags:
        created_post.tags.append(tag)

    db.commit()

    return created_post


@router.put("/{post_id}")
async def update_post(post_id: str, post: PostBody, response_model=Post):
    db = next(router.dependencies[0].dependency())

    existed_post = get_by_id(db, PostModel, post_id)

    if not existed_post:
        raise HTTPException(status_code=404, detail="Post not found")

    return update(db, existed_post, post)


@router.delete("/{post_id}")
async def delete_post(post_id: str) -> bool:
    db = next(router.dependencies[0].dependency())

    return delete(db, PostModel, post_id)