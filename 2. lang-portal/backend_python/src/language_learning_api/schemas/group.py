from pydantic import BaseModel

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    words_count: int

    class Config:
        from_attributes = True 