from fastapi import APIRouter, Depends, HTTPException
from db import get_db, get_all, get_by_id, create, update, delete

from models.category import Category as CategoryModel
from schemas.category import CategoryBody, Category


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    dependencies=[Depends(get_db)]
)


@router.get("/")
async def get_categories(offset: int = 0, limit: int = 100, response_model=list[Category]):
    db = next(router.dependencies[0].dependency())

    return get_all(db, CategoryModel, offset, limit)


@router.get("/{category_id}")
async def get_category(category_id: str, response_model=Category):
    db = next(router.dependencies[0].dependency())

    category = get_by_id(db, CategoryModel, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("/")
async def create_category(category: CategoryBody, response_model=Category):
    db = next(router.dependencies[0].dependency())

    new_category = CategoryModel(
        title = category.title
    )

    return create(db, new_category)


@router.put("/{category_id}")
async def update_category(category_id: str, category: CategoryBody, response_model=Category):
    db = next(router.dependencies[0].dependency())

    existed_category = get_by_id(db, CategoryModel, category_id)

    if not existed_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return update(db, existed_category, category)


@router.delete("/{category_id}")
async def delete_category(category_id: str, response_model=bool):
    db = next(router.dependencies[0].dependency())

    return delete(db, CategoryModel, category_id)