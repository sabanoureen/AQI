import requests

# Wah Cantt coordinates
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

print("\nLive Weather → Wah Cantt, Pakistan\n")
print(f"Temperature: {data['temperature_2m']} °C")
print(f"Humidity: {data['relative_humidity_2m']} %")
print(f"Pressure: {data['pressure_msl']} hPa")
print(f"Wind Speed: {data['wind_speed_10m']} m/s")
