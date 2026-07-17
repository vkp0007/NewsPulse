from fastapi import APIRouter

from database.mongodb import client

router = APIRouter()


@router.get("/health")
async def health():

    try:

        await client.admin.command("ping")

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:

        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
        }