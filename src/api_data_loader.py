import requests
import pandas as pd
from datetime import date, timedelta

LAT = 33.766
LON = 72.751

def fetch_historical_weather(days=150):
    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=days)

    url = (
        "https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={LAT}&longitude={LON}"
        f"&start_date={start_date}&end_date={end_date}"
        "&daily=temperature_2m_mean,relative_humidity_2m_mean,"
        "pressure_msl_mean,wind_speed_10m_mean"
        "&timezone=auto"
    )

    response = requests.get(url)
    response.raise_for_status()

    daily = response.json()["daily"]

    df = pd.DataFrame({
        "date": daily["time"],
        "temperature": daily["temperature_2m_mean"],
        "humidity": daily["relative_humidity_2m_mean"],
        "pressure": daily["pressure_msl_mean"],
        "wind_speed": daily["wind_speed_10m_mean"]
    })

    return df
