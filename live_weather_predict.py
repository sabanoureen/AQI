import joblib
import pandas as pd
from datetime import datetime, timedelta
import requests

# 1. Load trained model
model = joblib.load("models/weather_model.pkl")

# 2. Call live weather API (for demo trigger only)
LAT = 33.766
LON = 72.751

url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    "&current=temperature_2m"
)

_ = requests.get(url)  # just to show live API usage

# 3. Load historical data
df = pd.read_csv("data/wah_weather_5_months.csv")

# 4. Use recent mean values (last 7 days)
recent = df.tail(7)

X_demo = pd.DataFrame([{
    "humidity": recent["humidity"].mean(),
    "pressure": recent["pressure"].mean(),
    "wind_speed": recent["wind_speed"].mean()
}])

# 5. Predict next 3 days
pred = model.predict(X_demo)[0]

print("\nLive Weather → Next 3-Day Temperature Prediction (Demo)\n")

for i in range(1, 4):
    date = (datetime.today() + timedelta(days=i)).date()
    print(f"{date} → {pred:.2f} °C")
