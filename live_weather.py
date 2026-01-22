import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not set")

LAT = 33.766   # Wah Cantt
LON = 72.751

url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
)

response = requests.get(url)
response.raise_for_status()
data = response.json()
