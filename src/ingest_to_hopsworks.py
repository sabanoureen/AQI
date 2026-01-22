import hopsworks
import pandas as pd

project = hopsworks.login()
fs = project.get_feature_store()

# Load CSV
df = pd.read_csv("wah_weather_5_months.csv")

# FIX TYPES (VERY IMPORTANT)
df["date"] = pd.to_datetime(df["date"]).dt.date
df["temperature"] = df["temperature"].astype(float)
df["humidity"] = df["humidity"].astype(float)
df["pressure"] = df["pressure"].astype(float)
df["wind_speed"] = df["wind_speed"].astype(float)

# Get Feature Group
fg = fs.get_feature_group(
    name="wah_weather_features",
    version=1
)

# INSERT DATA
fg.insert(df, overwrite=True)

print("✅ DATA INGESTED SUCCESSFULLY")
