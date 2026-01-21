import requests

API_KEY = "YOUR_API_KEY"
CITY = "Wah Cantt"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

print("LIVE WEATHER")
print("Temperature:", data["main"]["temp"])
print("Humidity:", data["main"]["humidity"])
print("Pressure:", data["main"]["pressure"])
print("Wind Speed:", data["wind"]["speed"])
