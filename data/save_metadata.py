import os
from pymongo import MongoClient
from datetime import datetime
import sys

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    print("⚠️ MONGO_URI not set. Skipping MongoDB save.")
    sys.exit(0)   # <- VERY IMPORTANT (do NOT fail pipeline)

client = MongoClient(MONGO_URI)
db = client["weather_project"]
collection = db["model_metadata"]

metadata = {
    "model_name": "Decision Tree Regressor",
    "mae": 1.79,
    "trained_at": datetime.utcnow(),
    "is_best_model": True
}

collection.insert_one(metadata)
print("✅ Model metadata saved to MongoDB")
