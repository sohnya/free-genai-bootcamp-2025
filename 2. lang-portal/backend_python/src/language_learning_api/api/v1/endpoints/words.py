from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from .... import models, schemas
from ....db import get_db, crud

router = APIRouter()

@router.get("", response_model=schemas.PaginatedWords)
async def get_words(
    db: AsyncSession = Depends(get_db),
    page: int = Query(1, ge=1),
    sort_by: str = Query("kanji", regex="^(kanji|romaji|english|correct_count|wrong_count)$"),
    order: str = Query("asc", regex="^(asc|desc)$")
):
    return await crud.get_words(db, page=page, sort_by=sort_by, order=order) 