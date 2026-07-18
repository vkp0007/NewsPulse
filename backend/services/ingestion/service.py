import traceback

from repositories.article_repository import ArticleRepository

from services.clustering.cluster_service import ClusterService
from services.clustering.embedding_service import EmbeddingService

from services.ingestion.enrichment import enrich_articles
from services.ingestion.feeds import RSS_FEEDS
from services.ingestion.normalizer import normalize_entry
from services.ingestion.parser import fetch_feed

MAX_ARTICLES_PER_RUN = 10


async def fetch_articles():
    try:
        articles = []
        seen_urls = set()

        # Fetch and normalize RSS entries
        for source, url in RSS_FEEDS.items():

            feed = fetch_feed(url)

            for entry in feed.entries:

                article = normalize_entry(entry, source)

                if not article:
                    continue

                if article.url in seen_urls:
                    continue

                seen_urls.add(article.url)
                articles.append(article)

        # Extract article content
        articles = enrich_articles(articles)

        # Existing URLs
        existing_urls = await ArticleRepository.get_existing_urls()

        url_duplicates = 0
        new_articles = []

        for article in articles:

            if article.url in existing_urls:
                url_duplicates += 1
                continue

            if not article.content.strip():
                        continue

            new_articles.append(article)

        # Process only a limited number of articles
        new_articles = new_articles[:MAX_ARTICLES_PER_RUN]

        EmbeddingService.generate_embeddings(new_articles)

        clustering_result = {
            "clusters_created": 0,
            "clusters_updated": 0,
            "duplicates_skipped": 0,
        }

        inserted = 0

        if new_articles:

            clustering_result = await ClusterService.process_articles(
                 new_articles
            )

            articles_to_insert = clustering_result.pop("articles")

            inserted = len(articles_to_insert)

            await ArticleRepository.bulk_create(articles_to_insert)

        return {
                    "processed": len(articles),
                    "selected_for_processing": len(new_articles),
                    "inserted": inserted,
                    "url_duplicates": url_duplicates,
                    "semantic_duplicates": clustering_result["duplicates_skipped"],
                    "clusters_created": clustering_result["clusters_created"],
                    "clusters_updated": clustering_result["clusters_updated"],
            }

    except Exception:
        traceback.print_exc()
        raise