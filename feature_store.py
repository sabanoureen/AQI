# ============================
# FORCE HSFS ENGINE
# ============================
import os
os.environ["HSFS_ENGINE"] = "spark_no_metastore"

# ============================
# IMPORTS
# ============================
import hopsworks
import requests
import pandas as pd
from datetime import datetime

# ============================
# CONFIG (REPLACE VALUES ONLY)
# ============================
HOPSWORKS_API_KEY = "xXYlHTs57lHDDgfK.Q1KeHrFx6sxYeKe6w08etOftWxGegBSU8aQ1nGkerBcMasfFIqlhSJ6sLlEjnhQz"
OPENWEATHER_API_KEY = "21dee7321db2e7bf2ff36435abc1ab43"
CITY = "Wah Cantt,PK"

# ============================
# LOGIN TO HOPSWORKS
# ============================
project = hopsworks.login(api_key_value=HOPSWORKS_API_KEY)
fs = project.get_feature_store()
print("FEATURE STORE CONNECTED")

# ============================
# FETCH WEATHER
# ============================
url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
)

response = requests.get(url)
data = response.json()

df = pd.DataFrame([{
    "date": datetime.now().date().isoformat(),
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "pressure": data["main"]["pressure"],
    "wind_speed": data["wind"]["speed"]
}])

print(df)

# ============================
# FEATURE GROUP
# ============================
weather_fg = fs.get_or_create_feature_group(
    name="wah_weather_features",
    version=1,
    primary_key=["date"],
    description="Weather data for Wah Cantt Pakistan"
)

weather_fg.insert(df)
print("DATA INSERTED INTO FEATURE STORE")
