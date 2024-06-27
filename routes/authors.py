from fastapi import APIRouter, Depends, HTTPException
from werkzeug.security import generate_password_hash

from db import get_db, get_all, get_by_id, create, update, delete

from models.author import Author as AuthorModel
from schemas.author import AuthorBody, Author

from os import getenv
from dotenv import load_dotenv

load_dotenv()

HASH_METHOD = getenv('HASH_METHOD')


router = APIRouter(
    prefix="/authors",
    tags=["authors"],
    dependencies=[Depends(get_db)]
)


@router.get("/")
async def get_authors(offset: int = 0, limit: int = 100, response_model=list[Author]):
    db = next(router.dependencies[0].dependency())

    return get_all(db, AuthorModel, offset, limit)


@router.get("/{author_id}")
async def get_author(author_id: int, response_model=Author):
    db = next(router.dependencies[0].dependency())

    author = get_by_id(db, AuthorModel, author_id)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author


@router.post("/")
async def create_author(author: AuthorBody, response_model=Author):
    db = next(router.dependencies[0].dependency())

    new_author = AuthorModel(
        nickname = author.nickname, 
        email = author.email, 
        password = generate_password_hash(author.password, method=HASH_METHOD), 
        status = author.status
    )

    return create(db, new_author)


@router.put("/{author_id}")
async def update_author(author_id: str, author: AuthorBody, response_model=Author):
    db = next(router.dependencies[0].dependency())

    existed_author = get_by_id(db, AuthorModel, author_id)

    if not existed_author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return update(db, existed_author, author)


@router.delete("/{author_id}")
async def delete_author(author_id: str, response_model=bool):
    db = next(router.dependencies[0].dependency())

    return delete(db, AuthorModel, author_id)