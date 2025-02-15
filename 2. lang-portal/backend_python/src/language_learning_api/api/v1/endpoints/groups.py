from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from .... import models, schemas
from ....db import get_db, crud

router = APIRouter()

@router.get("", response_model=schemas.PaginatedGroups)
async def get_groups(
    db: AsyncSession = Depends(get_db),
    page: int = Query(1, ge=1),
    sort_by: str = Query("name", regex="^(name|words_count)$"),
    order: str = Query("asc", regex="^(asc|desc)$")
):
    return await crud.get_groups(db, page=page, sort_by=sort_by, order=order)

@router.get("/{group_id}", response_model=schemas.PaginatedWords)
async def get_group_words(
    group_id: int,
    db: AsyncSession = Depends(get_db),
    page: int = Query(1, ge=1),
    sort_by: str = Query("kanji", regex="^(kanji|romaji|english)$"),
    order: str = Query("asc", regex="^(asc|desc)$")
):
    return await crud.get_group_words(db, group_id=group_id, page=page, sort_by=sort_by, order=order) 