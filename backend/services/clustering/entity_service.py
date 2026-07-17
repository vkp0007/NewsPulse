import spacy


class EntityService:

    _nlp = None

    MAX_CONTENT_CHARS = 1500

    @classmethod
    def get_model(cls):

        if cls._nlp is None:
            cls._nlp = spacy.load("en_core_web_sm")

        return cls._nlp

    @classmethod
    def extract(
        cls,
        text,
    ):

        if not text:
            return set()

        doc = cls.get_model()(text)

        entities = set()

        for entity in doc.ents:

            if entity.label_ in {
                "PERSON",
                "ORG",
                "GPE",
                "LOC",
                "EVENT",
                "NORP",
            }:

                entities.add(
                    entity.text.lower().strip()
                )

        return entities

    @classmethod
    def overlap(
        cls,
        article,
        cluster,
    ):

        article_text = "\n".join(
            filter(
                None,
                [
                    article.title,
                    article.summary,
                    (article.content or "")[:cls.MAX_CONTENT_CHARS],
                ],
            )
        )

        article_entities = cls.extract(article_text)

        cluster_entities = set(
            cluster.get("entities", [])
        )

        if not article_entities or not cluster_entities:
            return 0.0

        intersection = (
            article_entities & cluster_entities
        )

        # Coverage of article entities
        return len(intersection) / len(article_entities)