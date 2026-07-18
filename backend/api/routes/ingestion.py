from fastapi import APIRouter, Header, HTTPException

from config import INGEST_API_KEY
from services.ingestion.service import fetch_articles

router = APIRouter()


@router.post("/ingest")
async def ingest(
    x_api_key: str = Header(None),
):

    if x_api_key != INGEST_API_KEY:
        raise HTTPException(
    status_code=401,
    detail="Unauthorized",
    )



    return await fetch_articles()