from pydantic import BaseModel
from typing import List
from .word import Word
from .group import Group

class PaginatedWords(BaseModel):
    items: List[Word]
    total: int
    page: int
    pages: int

class PaginatedGroups(BaseModel):
    items: List[Group]
    total: int
    page: int
    pages: int 