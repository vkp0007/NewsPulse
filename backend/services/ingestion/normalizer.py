from datetime import UTC, datetime
from email.utils import parsedate_to_datetime

from models.article import Article


def normalize_entry(entry, source):

    published = datetime.now(UTC)

    if getattr(entry, "published", None):

        try:

            published = parsedate_to_datetime(
                entry.published
            )

            if published.tzinfo is None:

                published = published.replace(
                    tzinfo=UTC
                )

            else:

                published = published.astimezone(
                    UTC
                )

        except Exception:

            published = datetime.now(UTC)

    return Article(

        title=getattr(entry, "title", ""),

        summary=getattr(entry, "summary", ""),

        content="",

        url=getattr(entry, "link", ""),

        source=source,

        published_at=published,
    )