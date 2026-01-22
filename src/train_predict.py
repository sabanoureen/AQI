import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load training data from Hopsworks export OR local df
from api_data_loader import fetch_historical_weather

df = fetch_historical_weather()
df.to_csv("data/generated_from_api.csv", index=False)



X = df[["humidity", "pressure", "wind_speed"]]
y = df["temperature"]

model = LinearRegression()
model.fit(X, y)

# Fake next 3 days (example live inputs)
future = np.array([
    [60, 1012, 4.2],
    [62, 1010, 3.9],
    [65, 1008, 5.1]
])

predictions = model.predict(future)

for i, temp in enumerate(predictions, 1):
    print(f"Day {i} predicted temperature: {temp:.2f} °C")
