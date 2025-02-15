from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db import Base

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    study_activity_id = Column(Integer, ForeignKey("study_activities.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    group = relationship("Group", back_populates="study_sessions")
    study_activity = relationship("StudyActivity", back_populates="study_sessions")
    review_items = relationship("WordReviewItem", back_populates="study_session") 