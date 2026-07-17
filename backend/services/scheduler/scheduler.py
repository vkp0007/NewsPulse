from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import SCHEDULER_INTERVAL
from services.ingestion.service import fetch_articles

scheduler = AsyncIOScheduler()


async def ingest_job():
    try:
        await fetch_articles()
    except Exception:
        # Handle or log the exception if needed
        pass


def start_scheduler():
    # Avoid duplicate job registration
    if scheduler.get_job("news_ingestion"):
        return

    scheduler.add_job(
        ingest_job,
        trigger="interval",
        minutes=SCHEDULER_INTERVAL,
        id="news_ingestion",
        replace_existing=True,
        max_instances=1,
        coalesce=True,
        misfire_grace_time=300,
    )

    scheduler.start()


def stop_scheduler():
    if scheduler.running:
        scheduler.shutdown(wait=False)