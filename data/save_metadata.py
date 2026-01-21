import os
from datetime import datetime
from pymongo import MongoClient

# Read MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI not set in environment variables")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["weather_project"]
collection = db["model_metadata"]

# Metadata for BEST model (Decision Tree)
metadata = {
    "model_name": "Decision Tree Regressor",
    "model_type": "DecisionTreeRegressor",
    "selection_reason": "Lowest MAE among 3 models",
    "mae": 1.79,
    "features": ["humidity", "pressure", "wind_speed"],
    "target": "temperature",
    "model_path": "models/best_weather_model.pkl",
    "trained_at": datetime.utcnow(),
    "is_best_model": True
}

# Insert metadata
result = collection.insert_one(metadata)

print("Best model metadata saved successfully")
print("Document ID:", result.inserted_id)
