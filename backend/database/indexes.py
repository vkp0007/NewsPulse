from database.mongodb import db


async def create_indexes():

    # Articles
    await db["articles"].create_index(
        "url",
        unique=True,
    )

    await db["articles"].create_index(
        "published_at",
    )

    await db["articles"].create_index(
        "source",
    )

    await db["articles"].create_index(
        "cluster_id",
    )

    # Clusters
    await db["clusters"].create_index(
        "updated_at",
    )

    await db["clusters"].create_index(
        "article_count",
    )