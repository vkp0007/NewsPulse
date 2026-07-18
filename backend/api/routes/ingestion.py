from fastapi import APIRouter, BackgroundTasks, Header, HTTPException

from config import INGEST_API_KEY
from services.ingestion.service import fetch_articles

router = APIRouter()


@router.post("/ingest")
async def ingest(
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None),
):
    if x_api_key != INGEST_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
     )

    # Run ingestion in the background
    background_tasks.add_task(fetch_articles)

    return {
        "status": "accepted",
        "message": "News ingestion started in the background."
    }