from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base

class StudyActivity(Base):
    __tablename__ = "study_activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

    # Relationships
    study_sessions = relationship("StudySession", back_populates="study_activity") 