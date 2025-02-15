from pydantic import BaseModel
from datetime import datetime

class WordReviewCreate(BaseModel):
    word_id: int
    correct: bool

class WordReview(WordReviewCreate):
    id: int
    study_session_id: int
    created_at: datetime

    class Config:
        from_attributes = True 