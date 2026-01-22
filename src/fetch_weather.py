import requests
import pandas as pd
from datetime import datetime, timedelta

# Wah Cantt coordinates
LATITUDE = 33.7667
LONGITUDE = 72.7500

# Date range (last 5 months)
end_date = datetime.now().date()
start_date = end_date - timedelta(days=150)

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "daily": [
        "temperature_2m_mean",
        "relative_humidity_2m_mean",
        "surface_pressure_mean",
        "wind_speed_10m_mean"
    ],
    "timezone": "Asia/Karachi"
}

response = requests.get(url, params=params)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame({
    "date": data["daily"]["time"],
    "temperature": data["daily"]["temperature_2m_mean"],
    "humidity": data["daily"]["relative_humidity_2m_mean"],
    "pressure": data["daily"]["surface_pressure_mean"],
    "wind_speed": data["daily"]["wind_speed_10m_mean"]
})

df.to_csv("wah_weather_5_months.csv", index=False)

print("CSV CREATED SUCCESSFULLY!")
print(df.head())
