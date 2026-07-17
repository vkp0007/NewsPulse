from bson import ObjectId

from database.mongodb import db


class ArticleRepository:

    collection = db["articles"]

    @staticmethod
    def serialize(document):

        if document:
            document["_id"] = str(document["_id"])

        return document

    @classmethod
    async def bulk_create(cls, articles):

        if not articles:
            return

        await cls.collection.insert_many(
            [
                article.model_dump()
                for article in articles
            ]
        )

    @classmethod
    async def get_existing_urls(cls):

        cursor = cls.collection.find(
            {},
            {
                "url": 1,
                "_id": 0,
            },
        )

        documents = await cursor.to_list(length=None)

        return {
            doc["url"]
            for doc in documents
        }

    @classmethod
    async def get_all(cls):

        cursor = cls.collection.find(
            {},
            {
                "embedding": 0,
            },
        ).sort(
            "published_at",
            -1,
        )

        documents = await cursor.to_list(length=None)

        return [
            cls.serialize(doc)
            for doc in documents
        ]

    @classmethod
    async def get_by_id(
        cls,
        article_id,
    ):

        document = await cls.collection.find_one(
            {
                "_id": ObjectId(article_id)
            },
            {
                "embedding": 0,
            },
        )

        return cls.serialize(document)

    @classmethod
    async def get_by_cluster(
        cls,
        cluster_id,
    ):

        cursor = cls.collection.find(
            {
                "cluster_id": cluster_id
            },
            {
                "embedding": 0,
            },
        ).sort(
            "published_at",
            -1,
        )

        documents = await cursor.to_list(length=None)

        return [
            cls.serialize(doc)
            for doc in documents
        ]

    @classmethod
    async def get_embeddings_by_cluster(
    cls,
    cluster_id,
    ):

        cursor = cls.collection.find(
           {
            "cluster_id": cluster_id
           },
         {
            "_id": 0,

            "title": 1,

            "source": 1,

            "embedding": 1,

            "url": 1,
           },
        )

        return await cursor.to_list(length=None)