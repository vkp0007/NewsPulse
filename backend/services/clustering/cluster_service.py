from datetime import UTC, datetime


from models.cluster import Cluster
from repositories.cluster_repository import ClusterRepository

from services.clustering.centroid_service import CentroidService
from services.clustering.similarity_service import SimilarityService
from services.duplicate.duplicate_service import DuplicateService
from services.clustering.scoring_service import ScoringService
from services.clustering.keyword_service import KeywordService
from services.clustering.entity_service import EntityService



class ClusterService:

   

    MAX_KEYWORDS = 50
    MAX_ENTITIES = 30

    @staticmethod
    def article_text(article):

        return " ".join(
            filter(
                None,
                [
                    article.title,
                    article.summary,
                ],
            )
        )

    @classmethod
    async def process_articles(
        cls,
        articles,
    ):

        created = 0
        updated = 0
        duplicates = 0

        articles_to_insert = []

        clusters = await ClusterRepository.get_all_for_clustering()

        for article in articles:

            result = await cls.assign_cluster(
                article,
                clusters,
            )

            if result == "created":

                created += 1
                articles_to_insert.append(article)

            elif result == "updated":

                updated += 1
                articles_to_insert.append(article)

            elif result == "duplicate":

                duplicates += 1

            else:

                raise ValueError(
                    f"Unknown cluster result: {result}"
                )

        return {

            "articles": articles_to_insert,

            "clusters_created": created,

            "clusters_updated": updated,

            "duplicates_skipped": duplicates,
        }
     
      
    @classmethod
    async def assign_cluster(
    cls,
    article,
    clusters,
    ):

     

     candidates = SimilarityService.find_top_k_clusters(
        article.embedding,
        clusters,
        k=5,
     )

    # --------------------------------------------------
    # No similar cluster found
    # --------------------------------------------------

     if not candidates:



        cluster = await cls.create_cluster(article)

        clusters.append(cluster)
        article.cluster_id = str(cluster["_id"])

        return "created"

    # --------------------------------------------------
    # Find best matching cluster
    # --------------------------------------------------

     best_cluster = None
     best_scores = None

     for cluster, cosine_score in candidates:

        scores = ScoringService.calculate(
            article,
            cluster,
            cosine_score,
        )

        if (
            best_scores is None
            or scores["final"] > best_scores["final"]
        ):
            best_scores = scores
            best_cluster = cluster

            # Safety check
     if best_cluster is None:
                raise RuntimeError("Failed to select a best cluster.")


            # --------------------------------------------------
            # Update existing cluster
            # --------------------------------------------------

     if ScoringService.should_update(best_scores):

                cluster_id = str(best_cluster["_id"])

                is_duplicate = await DuplicateService.is_duplicate(
                    article,
                    cluster_id,
                )

                if is_duplicate:

                    return "duplicate"

                

                await cls.update_cluster(
                    best_cluster,
                    article,
                )

                article.cluster_id = cluster_id

                return "updated"

                # --------------------------------------------------
                # Create new cluster
                # --------------------------------------------------


     cluster = await cls.create_cluster(article)

     clusters.append(cluster)

     article.cluster_id = str(cluster["_id"])

     return "created"


     
    @classmethod
    async def create_cluster(
        cls,
        article,
    ):

        text = cls.article_text(article)

        cluster = Cluster(

            title=article.title,

            summary=article.summary,

            embedding=article.embedding,

            keywords=sorted(
                KeywordService.extract(text)
            ),

            entities=sorted(
                EntityService.extract(text)
            ),

            sources=[article.source],

            article_count=1,

            start_time=article.published_at,

            end_time=article.published_at,
        )

        cluster_id = await ClusterRepository.create(
            cluster
        )

        cluster = cluster.model_dump()

        cluster["_id"] = cluster_id

        return cluster

    
    @classmethod
    async def update_cluster(
        cls,
        cluster,
        article,
    ):

        centroid = CentroidService.update_centroid(
            cluster["embedding"],
            article.embedding,
            cluster["article_count"],
        )

        text = cls.article_text(article)

        article_keywords = KeywordService.extract(
            text
        )

        article_entities = EntityService.extract(
            text
        )

        keywords = sorted(
            (
                set(cluster["keywords"])
                | article_keywords
            )
        )[:cls.MAX_KEYWORDS]

        entities = sorted(
            (
                set(cluster["entities"])
                | article_entities
            )
        )[:cls.MAX_ENTITIES]

        update = {

            "embedding": centroid,

            "keywords": keywords,

            "entities": entities,

            "sources": sorted(
                set(
                    cluster["sources"]
                    + [article.source]
                )
            ),

            "article_count":
                cluster["article_count"] + 1,

            "start_time": min(
                cluster["start_time"],
                article.published_at,
            ),

            "end_time": max(
                cluster["end_time"],
                article.published_at,
            ),

            "updated_at": datetime.now(UTC),
        }

        await ClusterRepository.update(
            str(cluster["_id"]),
            update,
        )

        cluster.update(update)