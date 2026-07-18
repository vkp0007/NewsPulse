import os

from dotenv import load_dotenv

load_dotenv()

# MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")

# Clustering
CLUSTER_THRESHOLD = float(
    os.getenv(
        "CLUSTER_THRESHOLD",
        "0.80",
    )
)

# API Security
INGEST_API_KEY = os.getenv("INGEST_API_KEY")