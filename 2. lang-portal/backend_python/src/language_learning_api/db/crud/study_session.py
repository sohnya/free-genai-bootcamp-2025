from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from ... import models, schemas

async def create_study_session(db: Session, session: schemas.StudySessionCreate):
    # Verify group exists
    group_query = select(models.Group).filter(models.Group.id == session.group_id)
    group_result = await db.execute(group_query)
    group = group_result.scalar_one_or_none()
    
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    # Verify study activity exists
    activity_query = select(models.StudyActivity).filter(models.StudyActivity.id == session.study_activity_id)
    activity_result = await db.execute(activity_query)
    activity = activity_result.scalar_one_or_none()
    
    if not activity:
        raise HTTPException(status_code=404, detail="Study activity not found")
    
    db_session = models.StudySession(**session.dict())
    db.add(db_session)
    await db.flush()
    await db.refresh(db_session)
    return db_session 