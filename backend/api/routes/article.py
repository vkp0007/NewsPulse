from fastapi import APIRouter, HTTPException

from repositories.article_repository import ArticleRepository

router = APIRouter()


@router.get("/articles")
async def get_articles():

    articles = await ArticleRepository.get_all()

    return {
     "count": len(articles),
     "articles": articles,
    }


@router.get("/articles/{article_id}")
async def get_article(article_id: str):

    article = await ArticleRepository.get_by_id(
        article_id
    )

    if not article:
        raise HTTPException(
           status_code=404,
         detail="Article not found",
        )

    return article


    # -----------------------------
    # NEW ENDPOINT
    # -----------------------------
@router.get("/articles/cluster/{cluster_id}")
async def get_articles_by_cluster(cluster_id: str):

    articles = await ArticleRepository.get_by_cluster(
        cluster_id
    )

    return {
         "count": len(articles),
         "articles": articles,
    }