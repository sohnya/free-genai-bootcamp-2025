from fastapi import FastAPI
from .db import engine
from . import models
from .api.v1.api import api_router

app = FastAPI(title="Language Learning API")

@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

app.include_router(api_router, prefix="/v1") 