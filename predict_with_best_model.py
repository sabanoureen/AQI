import os
import joblib
import pandas as pd
from pymongo import MongoClient
from datetime import datetime, timedelta

# 1️⃣ MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["weather_project"]
collection = db["model_metadata"]

# 2️⃣ Fetch BEST model metadata
best_model_meta = collection.find_one({"is_best_model": True})

if not best_model_meta:
    raise ValueError("No best model found in metadata")

model_path = best_model_meta["model_path"]
model_name = best_model_meta["model_name"]

print(f"\nUsing BEST model: {model_name}")

# 3️⃣ Load model
model = joblib.load(model_path)

# 4️⃣ Demo input (mean realistic values)
X_demo = pd.DataFrame([{
    "humidity": 70,
    "pressure": 1010,
    "wind_speed": 5
}])

# 5️⃣ Predict next 3 days
prediction = model.predict(X_demo)[0]

print("\nNext 3-Day Temperature Prediction (Demo):\n")
for i in range(1, 4):
    date = (datetime.today() + timedelta(days=i)).date()
    print(f"{date} → {prediction:.2f} °C")
