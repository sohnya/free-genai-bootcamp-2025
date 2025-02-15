from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from ... import models, schemas

async def create_word_review(db: Session, session_id: int, review: schemas.WordReviewCreate):
    # Verify session exists and is active
    session_query = select(models.StudySession).filter(models.StudySession.id == session_id)
    session_result = await db.execute(session_query)
    session = session_result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(status_code=404, detail="Study session not found")
    
    # Verify word exists and belongs to the session's group
    word_query = select(models.Word).join(models.WordGroup).filter(
        models.Word.id == review.word_id,
        models.WordGroup.group_id == session.group_id
    )
    word_result = await db.execute(word_query)
    word = word_result.scalar_one_or_none()
    
    if not word:
        raise HTTPException(
            status_code=404, 
            detail="Word not found or does not belong to the session's group"
        )
    
    db_review = models.WordReviewItem(
        word_id=review.word_id,
        study_session_id=session_id,
        correct=review.correct
    )
    db.add(db_review)
    await db.flush()
    await db.refresh(db_review)
    return db_review 