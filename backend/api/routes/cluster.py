from fastapi import APIRouter, HTTPException

from repositories.article_repository import ArticleRepository
from repositories.cluster_repository import ClusterRepository

router = APIRouter()


@router.get("/clusters")
async def get_clusters():

    clusters = await ClusterRepository.get_all()

    return {
        "success": True,
        "count": len(clusters),
        "clusters": clusters,
    }


@router.get("/clusters/{cluster_id}")
async def get_cluster(cluster_id: str):

    cluster = await ClusterRepository.get_by_id(
        cluster_id
    )

    if not cluster:

        raise HTTPException(
            status_code=404,
            detail="Cluster not found",
        )

    articles = await ArticleRepository.get_by_cluster(
        cluster_id
    )

    return {
        "cluster": cluster,
        "articles": articles,
    }