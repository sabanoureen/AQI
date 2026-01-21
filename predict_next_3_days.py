import joblib
import pandas as pd
from datetime import datetime, timedelta

# 1. Load trained model
model = joblib.load("models/weather_model.pkl")

# 2. Use last known weather values (demo input)
last_known = {
    "humidity": 75,
    "pressure": 952,
    "wind_speed": 5
}

# 3. Create next 3 days input
future_dates = [datetime.today() + timedelta(days=i) for i in range(1, 4)]

X_future = pd.DataFrame([last_known] * 3)

# 4. Predict temperatures
predictions = model.predict(X_future)

# 5. Display results
print("\nNext 3-Day Temperature Prediction (Demo):\n")
for date, temp in zip(future_dates, predictions):
    print(f"{date.date()} → {temp:.2f} °C")
