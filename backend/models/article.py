from datetime import UTC, datetime
from typing import Optional

from pydantic import BaseModel, Field


class Article(BaseModel):

    title: str

    summary: str = ""

    content: str = ""

    url: str

    source: str

    published_at: datetime

    author: Optional[str] = None

    image_url: Optional[str] = None

    embedding: Optional[list[float]] = None

    cluster_id: Optional[str] = None

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )