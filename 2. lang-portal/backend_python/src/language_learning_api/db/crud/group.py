from sqlalchemy.orm import Session, selectinload
from sqlalchemy import desc, select, func
from fastapi import HTTPException
from ... import models
import math
from .base import ITEMS_PER_PAGE

async def get_groups(db: Session, page: int = 1, sort_by: str = "name", order: str = "asc"):
    # Validate sort_by field
    if sort_by not in ['name', 'words_count']:
        sort_by = 'name'  # Default to name if invalid field
    
    query = select(models.Group)
    
    if order == "desc":
        query = query.order_by(desc(getattr(models.Group, sort_by)))
    else:
        query = query.order_by(getattr(models.Group, sort_by))
    
    count_result = await db.execute(select(func.count()).select_from(models.Group))
    total = count_result.scalar()
    pages = math.ceil(total / ITEMS_PER_PAGE)
    
    result = await db.execute(
        query.offset((page - 1) * ITEMS_PER_PAGE).limit(ITEMS_PER_PAGE)
    )
    items = result.scalars().all()
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "pages": pages
    }

async def get_group_words(db: Session, group_id: int, page: int = 1, sort_by: str = "kanji", order: str = "asc"):
    try:
        # Verify group exists
        group_query = select(models.Group).filter(models.Group.id == group_id)
        group_result = await db.execute(group_query)
        group = group_result.scalar_one_or_none()
        
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        
        # Build query for words in group with eager loading
        query = (
            select(models.Word)
            .join(models.WordGroup)
            .filter(models.WordGroup.group_id == group_id)
            .options(selectinload(models.Word.review_items))
        )
        
        # Apply sorting
        if order == "desc":
            query = query.order_by(desc(getattr(models.Word, sort_by)))
        else:
            query = query.order_by(getattr(models.Word, sort_by))
        
        # Get total count
        count_result = await db.execute(
            select(func.count())
            .select_from(models.Word)
            .join(models.WordGroup)
            .filter(models.WordGroup.group_id == group_id)
        )
        total = count_result.scalar()
        pages = math.ceil(total / ITEMS_PER_PAGE)
        
        # Get paginated results
        result = await db.execute(
            query.offset((page - 1) * ITEMS_PER_PAGE).limit(ITEMS_PER_PAGE)
        )
        items = result.scalars().all()
        
        # Convert to dicts to avoid async property issues
        items = [item.to_dict() for item in items]
        
        return {
            "items": items,
            "total": total,
            "page": page,
            "pages": pages
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in get_group_words: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving group words: {str(e)}"
        ) 