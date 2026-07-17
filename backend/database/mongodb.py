import os
from datetime import UTC

from dotenv import load_dotenv
from pymongo import AsyncMongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError(
        "MONGODB_URI is not configured."
    )

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "newspulse_ai",
)

client = AsyncMongoClient(
    MONGODB_URI,
    tz_aware=True,
    tzinfo=UTC,
)

db = client[DATABASE_NAME]