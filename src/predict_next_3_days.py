import requests
import pandas as pd
import joblib
from datetime import datetime, timedelta

# Load best model
model = joblib.load("models/best_weather_model.pkl")

LAT = 33.766
LON = 72.751

url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    "&current=relative_humidity_2m,pressure_msl,wind_speed_10m"
)

response = requests.get(url)
response.raise_for_status()
data = response.json()["current"]

X_live = pd.DataFrame([{
    "humidity": data["relative_humidity_2m"],
    "pressure": data["pressure_msl"],
    "wind_speed": data["wind_speed_10m"]
}])

prediction = model.predict(X_live)[0]

print("\nNext 3-Day Temperature Prediction for Wah Cantt:\n")
for i in range(1, 4):
    date = (datetime.today() + timedelta(days=i)).date()
    print(f"{date} → {prediction:.2f} °C")
