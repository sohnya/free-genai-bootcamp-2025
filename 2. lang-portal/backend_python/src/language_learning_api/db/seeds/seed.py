import asyncio
import csv
import json
from pathlib import Path
import sys
from sqlalchemy import select

# Add parent directory to path so we can import our models
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from language_learning_api.db import engine, SessionLocal
from language_learning_api import models

# Update seed directory path
SEED_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "data" / "seeds"

async def seed_words():
    async with SessionLocal() as session:
        with open(SEED_DIR / 'words.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Handle empty parts
                parts = None
                if row['parts'] and row['parts'].strip():  # Only parse if not empty
                    parts = json.loads(row['parts'])
                
                word = models.Word(
                    kanji=row['kanji'],
                    romaji=row['romaji'],
                    english=row['english'],
                    parts=parts  # Will be None if parts was empty
                )
                session.add(word)
        await session.commit()

async def seed_groups():
    async with SessionLocal() as session:
        with open(SEED_DIR / 'groups.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                group = models.Group(name=row['name'])
                session.add(group)
        await session.commit()

async def seed_word_groups():
    async with SessionLocal() as session:
        with open(SEED_DIR / 'word_groups.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Strip whitespace and find word and group
                word_query = select(models.Word).filter(models.Word.kanji == row['word_kanji'].strip())
                group_query = select(models.Group).filter(models.Group.name == row['group_name'].strip())
                
                word_result = await session.execute(word_query)
                group_result = await session.execute(group_query)
                
                try:
                    word = word_result.scalar_one()
                    group = group_result.scalar_one()
                except Exception as e:
                    print(f"Error processing row: {row}")
                    print(f"Word kanji: '{row['word_kanji'].strip()}'")
                    print(f"Group name: '{row['group_name'].strip()}'")
                    raise
                
                # Create word_group
                word_group = models.WordGroup(word_id=word.id, group_id=group.id)
                session.add(word_group)
        await session.commit()

async def seed_study_activities():
    async with SessionLocal() as session:
        with open(SEED_DIR / 'study_activities.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                activity = models.StudyActivity(
                    name=row['name'],
                    url=row['url']
                )
                session.add(activity)
        await session.commit()

async def seed_all():
    async with engine.begin() as conn:
        # Drop and recreate all tables
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)
    
    # Seed all data
    await seed_words()
    await seed_groups()
    await seed_word_groups()
    await seed_study_activities()

if __name__ == "__main__":
    asyncio.run(seed_all()) 