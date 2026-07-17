from fastapi import APIRouter

from services.ingestion.service import fetch_articles

router = APIRouter()


@router.post("/ingest")
async def ingest():

    return await fetch_articles()