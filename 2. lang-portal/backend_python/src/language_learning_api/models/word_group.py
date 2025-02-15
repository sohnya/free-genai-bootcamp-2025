from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, text
from ..db import Base
from sqlalchemy import event
from sqlalchemy.orm import Session

class WordGroup(Base):
    __tablename__ = "word_groups"

    word_id = Column(Integer, ForeignKey("words.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)

    __table_args__ = (UniqueConstraint('word_id', 'group_id', name='unique_word_group'),)

@event.listens_for(WordGroup, 'after_insert')
async def update_word_count_on_insert(mapper, connection, target):
    await connection.execute(
        text("UPDATE groups SET words_count = words_count + 1 WHERE id = :group_id"),
        {"group_id": target.group_id}
    )

@event.listens_for(WordGroup, 'after_delete')
async def update_word_count_on_delete(mapper, connection, target):
    await connection.execute(
        text("UPDATE groups SET words_count = words_count - 1 WHERE id = :group_id"),
        {"group_id": target.group_id}
    ) 