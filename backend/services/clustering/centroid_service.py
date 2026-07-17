class CentroidService:

    @staticmethod
    def update_centroid(
        centroid,
        embedding,
        article_count,
    ):

        if len(centroid) != len(embedding):
            raise ValueError(
                "Embedding dimensions do not match."
            )

        return [
            (c * article_count + e)
            / (article_count + 1)
            for c, e in zip(
                centroid,
                embedding,
            )
        ]