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
        Returns embeddings.
        """

        cursor = cls.collection.find().sort(
            "updated_at",
            -1,
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