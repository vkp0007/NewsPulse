from concurrent.futures import ThreadPoolExecutor

from services.ingestion.extractor import extract_article


MAX_WORKERS = 8


def enrich_articles(articles):

    def enrich(article):

        article.content = extract_article(article.url)

        return article

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        return list(
            executor.map(
                enrich,
                articles,
            )
        )