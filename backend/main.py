from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.article import router as article_router
from api.routes.cluster import router as cluster_router
from api.routes.health import router as health_router
from api.routes.ingestion import router as ingestion_router

from database.indexes import create_indexes
from database.mongodb import client




from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_indexes()
    yield
    await client.close()


app = FastAPI(
        title="NewsPulse AI",
        version="1.0.0",
        lifespan=lifespan,
)

    # -------------------------
    # CORS
    # -------------------------

app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "https://newspulse-ai-two.vercel.app",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

    # -------------------------
    # Register Routes
    # -------------------------

app.include_router(
        health_router,
        tags=["Health"],
)

app.include_router(
        ingestion_router,
        prefix="/api",
        tags=["Ingestion"],
)

app.include_router(
        article_router,
        prefix="/api",
        tags=["Articles"],
)

app.include_router(
        cluster_router,
        prefix="/api",
        tags=["Clusters"],
)


@app.get("/")
async def root():

    return {
"message": "Welcome to NewsPulse AI 🚀",
"docs": "/docs",
"version": "1.0.0",
}