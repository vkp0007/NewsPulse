from datetime import datetime, timedelta, UTC

from bson import ObjectId

from database.mongodb import db


class ClusterRepository:

    collection = db["clusters"]

    @staticmethod
    def serialize(document):

        if document:
            document["_id"] = str(document["_id"])

        return document

    @classmethod
    async def create(cls, cluster):

        result = await cls.collection.insert_one(
            cluster.model_dump()
        )

        return str(result.inserted_id)

    @classmethod
    async def get_all(cls):
        """
        Used by API.
        Does not return embeddings.
        """

        cursor = cls.collection.find(
            {},
            {
                "embedding": 0,
            },
        ).sort(
            "updated_at",
            -1,
        )

        documents = await cursor.to_list(length=None)

        return [
             cls.serialize(doc)
             for doc in documents
        ]      

    @classmethod
    async def get_all_for_clustering(cls):
        """
        Used internally by ClusterService.
        Returns only clusters updated in the last 24 hours.
        """

        cutoff = datetime.now(UTC) - timedelta(days=1)

        projection = {
            "_id": 1,
            "embedding": 1,
            "keywords": 1,
            "entities": 1,
            "sources": 1,
            "article_count": 1,
            "start_time": 1,
            "end_time": 1,
            "updated_at": 1,
        }

        cursor = (
            cls.collection.find(
                {
                    "updated_at": {"$gte": cutoff}
                },
                projection,
            )
            .sort("updated_at", -1)
        )

        return await cursor.to_list(length=None)

    @classmethod
    async def get_by_id(
        cls,
        cluster_id,
    ):

        document = await cls.collection.find_one(
            {
                "_id": ObjectId(cluster_id)
            },
            {
                "embedding": 0,
            },
        )

        return cls.serialize(document)

    @classmethod
    async def update(
        cls,
        cluster_id,
        update,
    ):

        await cls.collection.update_one(
            {
                "_id": ObjectId(cluster_id)
            },
            {
                "$set": update
            },
        )