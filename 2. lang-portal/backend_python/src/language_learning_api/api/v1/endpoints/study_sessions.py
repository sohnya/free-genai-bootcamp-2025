from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .... import models, schemas
from ....db import get_db, crud

router = APIRouter()

@router.post("", response_model=schemas.StudySession)
async def create_study_session(
    session: schemas.StudySessionCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_study_session(db=db, session=session)

@router.post("/{session_id}/review", response_model=schemas.WordReview)
async def create_word_review(
    session_id: int,
    review: schemas.WordReviewCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_word_review(db=db, session_id=session_id, review=review) 