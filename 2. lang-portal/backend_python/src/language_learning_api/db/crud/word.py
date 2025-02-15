from sqlalchemy.orm import Session, selectinload
from sqlalchemy import desc, select, func
from ... import models
import math
from .base import ITEMS_PER_PAGE
from fastapi import HTTPException

async def get_words(db: Session, page: int = 1, sort_by: str = "kanji", order: str = "asc"):
    try:
        # Build base query with eager loading of review_items
        query = select(models.Word).options(selectinload(models.Word.review_items))
        
        # Only allow sorting by basic fields for now
        if sort_by not in ['kanji', 'romaji', 'english']:
            sort_by = 'kanji'  # Default to kanji if invalid sort field
        
        # Apply sorting
        if order == "desc":
            query = query.order_by(desc(getattr(models.Word, sort_by)))
        else:
            query = query.order_by(getattr(models.Word, sort_by))
        
        # Get total count
        count_result = await db.execute(select(func.count()).select_from(models.Word))
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
    except Exception as e:
        print(f"Error in get_words: {str(e)}")  # Log the error
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving words: {str(e)}"
        ) 