from sentence_transformers import SentenceTransformer


class EmbeddingService:

    _model = None

    MODEL_NAME = "all-MiniLM-L6-v2"

    MAX_CONTENT_CHARS = 1500

    @classmethod
    def get_model(cls):
        """
        Load the embedding model only once.
        """

        if cls._model is None:

            

            cls._model = SentenceTransformer(
                cls.MODEL_NAME
            )

            

        return cls._model

    @classmethod
    def generate_embeddings(
        cls,
        articles,
    ):
        """
        Generate embeddings for all articles in a single batch.
        """

        if not articles:
            
            return

        texts = []



        # --------------------------------------------------
        # Prepare texts
        # --------------------------------------------------

        for article in articles:

            title = (article.title or "").strip()

            summary = (article.summary or "").strip()

            content = (
                (article.content or "")
                [: cls.MAX_CONTENT_CHARS]
                .strip()
            )

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


            # --------------------------------------------------
            # Generate embeddings (ONE BATCH)
            # --------------------------------------------------

        model = cls.get_model()

        embeddings = model.encode(
                texts,
                batch_size=4,
                normalize_embeddings=True,
                show_progress_bar=False,
            )

            # --------------------------------------------------
            # Assign embeddings
            # --------------------------------------------------

        for article, embedding in zip(
                articles,
                embeddings,
            ):

                article.embedding = embedding.tolist()
