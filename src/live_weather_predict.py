import joblib
import pandas as pd
from datetime import datetime, timedelta
import requests

# Load best trained model
model = joblib.load("models/weather_model.pkl")

# Wah Cantt coordinates
LAT = 33.766
LON = 72.751

# Fetch live + recent data (Open-Meteo)
url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    "&hourly=relative_humidity_2m,pressure_msl,wind_speed_10m"
    "&past_days=7"
    "&timezone=auto"
)

response = requests.get(url)
response.raise_for_status()
data = response.json()["hourly"]

df = pd.DataFrame({
    "humidity": data["relative_humidity_2m"],
    "pressure": data["pressure_msl"],
    "wind_speed": data["wind_speed_10m"]
})

# Use recent mean values
X_live = pd.DataFrame([{
    "humidity": df["humidity"].mean(),
    "pressure": df["pressure"].mean(),
    "wind_speed": df["wind_speed"].mean()
}])

# Predict
prediction = model.predict(X_live)[0]

print("\nLive Weather → Next 3-Day Temperature Prediction for Wah Cantt\n")

for i in range(1, 4):
    date = (datetime.today() + timedelta(days=i)).date()
    print(f"{date} → {prediction:.2f} °C")

