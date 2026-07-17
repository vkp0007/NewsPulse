from services.clustering.entity_service import EntityService
from services.clustering.keyword_service import KeywordService


class ScoringService:

    COSINE_WEIGHT = 0.85
    KEYWORD_WEIGHT = 0.10
    ENTITY_WEIGHT = 0.05

    UPDATE_THRESHOLD = 0.45

    HIGH_CONFIDENCE = 0.70

    @classmethod
    def calculate(
        cls,
        article,
        cluster,
        cosine_score,
    ):

        keyword_score = KeywordService.overlap(
            article,
            cluster,
        )

        entity_score = EntityService.overlap(
            article,
            cluster,
        )

        final_score = (
            cls.COSINE_WEIGHT * cosine_score
            + cls.KEYWORD_WEIGHT * keyword_score
            + cls.ENTITY_WEIGHT * entity_score
        )

        return {
    "cosine": cosine_score,
    "keyword": keyword_score,
    "entity": entity_score,
    "final": final_score,
}

    @classmethod
    def should_update(
        cls,
        scores,
    ):

        cosine = scores["cosine"]
        keyword = scores["keyword"]
        entity = scores["entity"]
        final = scores["final"]

        # Very strong semantic match
        if cosine >= cls.HIGH_CONFIDENCE:
            return True

        # Strong semantic + entity support
        if (
            cosine >= 0.60
            and entity >= 0.10
        ):
            return True

        # Strong semantic + keyword support
        if (
            cosine >= 0.55
            and keyword >= 0.10
        ):
            return True

        # Moderate semantic + both signals
        if (
            cosine >= 0.50
            and keyword >= 0.08
            and entity >= 0.08
        ):
            return True

        # Overall weighted score
        if final >= cls.UPDATE_THRESHOLD:
            return True

        return False