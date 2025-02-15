from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from ..db import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    kanji = Column(String, nullable=False)
    romaji = Column(String, nullable=False)
    english = Column(String, nullable=False)
    parts = Column(JSON, nullable=True)

    # Relationships
    groups = relationship("Group", secondary="word_groups", back_populates="words")
    review_items = relationship("WordReviewItem", back_populates="word")

    # Make these regular properties instead of async
    @property
    def correct_count(self):
        if not self.review_items:
            return 0
        return len([r for r in self.review_items if r.correct])

    @property
    def wrong_count(self):
        if not self.review_items:
            return 0
        return len([r for r in self.review_items if not r.correct])

    def to_dict(self):
        return {
            "id": self.id,
            "kanji": self.kanji,
            "romaji": self.romaji,
            "english": self.english,
            "parts": self.parts,
            "correct_count": self.correct_count,
            "wrong_count": self.wrong_count
        } 