import re

from repositories.article_repository import ArticleRepository
from services.clustering.similarity_service import SimilarityService


class DuplicateService:

    THRESHOLD = 0.93

    @staticmethod
    def normalize_title(
        title,
    ):

        title = title.lower()

        title = re.sub(
            r"[^a-z0-9\s]",
            "",
            title,
        )

        return " ".join(
            title.split()
        )

    @classmethod
    async def is_duplicate(
    cls,
    article,
    cluster_id,
    ):

       articles = await ArticleRepository.get_embeddings_by_cluster(
        cluster_id
        )

       

       article_title = cls.normalize_title(
            article.title
        )

       for existing in articles:

            if not existing.get("embedding"):
                continue

            if cls.normalize_title(
                existing["title"]
            ) == article_title:

                return True

            score = SimilarityService.calculate(
                article.embedding,
                existing["embedding"],
            )


            if score >= cls.THRESHOLD:

                return True

       return False