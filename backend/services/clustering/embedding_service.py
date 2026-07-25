from sentence_transformers import SentenceTransformer


class EmbeddingService:

    _model = None

    MODEL_NAME = "sentence-transformers/paraphrase-MiniLM-L3-v2"
    MAX_CONTENT_CHARS = 1500

    @classmethod
    def get_model(cls):
        """
        Load the embedding model only once.
        """
        if cls._model is None:
            print("STEP 1", flush=True)

            cls._model = SentenceTransformer(cls.MODEL_NAME)

            print("STEP 2", flush=True)

        return cls._model

    @classmethod
    def generate_embeddings(cls, articles):
        """
        Generate embeddings with minimal memory usage.
        """

        if not articles:
            return

        texts = []

        for article in articles:

            title = (article.title or "").strip()
            summary = (article.summary or "").strip()
            content = (article.content or "")[:cls.MAX_CONTENT_CHARS].strip()

            text = "\n".join(
                filter(
                    None,
                    [
                        title,
                        summary,
                        content,
                    ],
                )
            )

            texts.append(text)

        model = cls.get_model()

        print("STEP 3", flush=True)

        embeddings = model.encode(
                texts,
                batch_size=1,
                convert_to_numpy=False,
                normalize_embeddings=True,
                show_progress_bar=False,
        )

        print("STEP 4", flush=True)

        for article, embedding in zip(articles, embeddings):
            article.embedding = embedding.cpu().tolist()

        print("STEP 5", flush=True)