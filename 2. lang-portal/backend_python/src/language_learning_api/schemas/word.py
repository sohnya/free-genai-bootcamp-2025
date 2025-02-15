from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class WordBase(BaseModel):
    kanji: str
    romaji: str
    english: str
    parts: Optional[Dict[str, Any]] = None

class WordCreate(WordBase):
    pass

class Word(WordBase):
    id: int
    correct_count: int = 0
    wrong_count: int = 0
    
    class Config:
        from_attributes = True 

class PaginatedWords(BaseModel):
    items: List[Dict[str, Any]]  # Changed from List[Word] to List[Dict]
    total: int
    page: int
    pages: int 