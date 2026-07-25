from sklearn.feature_extraction.text import HashingVectorizer


class EmbeddingService:

    vectorizer = HashingVectorizer(
        n_features=512,
        stop_words="english",
        alternate_sign=False,
        norm="l2",
    )

    MAX_CONTENT_CHARS = 1500

    @classmethod
    def generate_embeddings(cls, articles):

        if not articles:
            return

        texts = []

        for article in articles:

            text = " ".join(
                filter(
                    None,
                    [
                        article.title,
                        article.summary,
                        (article.content or "")[:cls.MAX_CONTENT_CHARS],
                    ],
                )
            )

            texts.append(text)

        vectors = cls.vectorizer.transform(texts)

        for article, vector in zip(articles, vectors):
            article.embedding = vector.toarray()[0].tolist()