from sklearn.metrics.pairwise import cosine_similarity


class SimilarityService:

    MIN_COSINE_SCORE = 0.30

    @staticmethod
    def calculate(
        embedding1,
        embedding2,
    ):
        """
        Calculate cosine similarity between two normalized embeddings.
        """

        return float(
          cosine_similarity(
              [embedding1],
              [embedding2],
          )[0][0]
        )

    @classmethod
    def find_best_cluster(
        cls,
        embedding,
        clusters,
    ):
        """
        Return the single best matching cluster.
        """

        candidates = cls.find_top_k_clusters(
            embedding,
            clusters,
            k=1,
        )

        if not candidates:
            return None, 0.0

        return candidates[0]

    @classmethod
    def find_top_k_clusters(
        cls,
        embedding,
        clusters,
        k=5,
    ):
        """
        Return the top-k clusters above the minimum cosine threshold.
        """

        if not clusters:
            return []

        candidates = []

        for cluster in clusters:

            cluster_embedding = cluster.get(
                "embedding"
            )

            if not cluster_embedding:
                continue

            score = cls.calculate(
                embedding,
                cluster_embedding,
            )

            if score >= cls.MIN_COSINE_SCORE:

                candidates.append(
                    (
                        cluster,
                        score,
                    )
                )

        candidates.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        return candidates[:k]