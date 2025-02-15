from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    words_count = Column(Integer, default=0)

    # Relationships
    words = relationship("Word", secondary="word_groups", back_populates="groups")
    study_sessions = relationship("StudySession", back_populates="group") 