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

# Scheduler
SCHEDULER_INTERVAL = int(
    os.getenv(
        "SCHEDULER_INTERVAL",
        "30",
    )
)