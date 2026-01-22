import os
from datetime import datetime
from pymongo import MongoClient

# Read Mongo URI
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI not set in environment variables")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["weather_project"]
collection = db["model_metadata"]

# ✅ DEFINE metadata (THIS WAS MISSING)
metadata = {
    "model_name": "linear_regression_v1",
    "model_type": "LinearRegression",
    "features_used": ["humidity", "pressure", "wind_speed"],
    "target": "temperature",
    "metrics": {
        "rmse": 2.3,
        "r2": 0.71
    },
    "trained_on": "wah_weather_5_months.csv",
    "created_at": datetime.utcnow()
}

# Insert into MongoDB
result = collection.insert_one(metadata)

print("✅ Model metadata saved successfully!")
print("📌 Inserted document ID:", result.inserted_id)
