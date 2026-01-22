import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import os

# Load dataset
from api_data_loader import fetch_historical_weather

df = fetch_historical_weather()

# optional logging only
df.to_csv("data/generated_from_api.csv", index=False)

# continue with training


X = df[["humidity", "pressure", "wind_speed"]]
y = df["temperature"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train BEST model (Decision Tree)
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f"Best Model: Decision Tree")
print(f"MAE: {mae:.2f}")

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/best_weather_model.pkl")

print("Best model saved to models/best_weather_model.pkl")
