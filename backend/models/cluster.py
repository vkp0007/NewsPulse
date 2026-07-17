from datetime import UTC, datetime

from pydantic import BaseModel, Field


class Cluster(BaseModel):

    title: str

    summary: str

    embedding: list[float]

    keywords: list[str] = Field(
        default_factory=list
    )

    entities: list[str] = Field(
        default_factory=list
    )

    sources: list[str] = Field(
        default_factory=list
    )

    article_count: int = 1

    start_time: datetime

    end_time: datetime

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )