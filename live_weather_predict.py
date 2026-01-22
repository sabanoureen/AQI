import requests

LAT = 33.766
LON = 72.751

url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    "&current=temperature_2m,relative_humidity_2m,pressure_msl,wind_speed_10m"
)

response = requests.get(url)
response.raise_for_status()

data = response.json()["current"]

live_weather = {
    "temperature": data["temperature_2m"],
    "humidity": data["relative_humidity_2m"],
    "pressure": data["pressure_msl"],
    "wind_speed": data["wind_speed_10m"]
}

print("Live Weather in Wah Cantt:")
print(live_weather)
