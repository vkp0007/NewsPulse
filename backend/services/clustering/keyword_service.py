import re
import spacy


class KeywordService:

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
        text: str,
    ):

        text = re.sub(
            r"\s+",
            " ",
            text.strip(),
        )

        if not text:
            return set()

        doc = cls.get_model()(text)

        keywords = set()

        for token in doc:

            if (
                token.is_stop
                or token.is_punct
                or token.is_space
                or token.like_num
            ):
                continue

            lemma = token.lemma_.lower().strip()

            if len(lemma) < 3:
                continue

            keywords.add(lemma)

        return keywords

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

        article_keywords = cls.extract(article_text)

        cluster_keywords = set(
            cluster.get("keywords", [])
        )

        if not article_keywords or not cluster_keywords:
            return 0.0

        intersection = (
            article_keywords & cluster_keywords
        )

        # Coverage of article keywords
        return len(intersection) / len(article_keywords)