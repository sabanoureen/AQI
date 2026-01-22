import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib
import os

# 1. Load data
df = pd.read_csv("data/wah_weather_5_months.csv")

# 2. Features and label
X = df[["humidity", "pressure", "wind_speed"]]
y = df["temperature"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print("Model trained successfully")
print(f"Mean Absolute Error: {mae:.2f}")

# 6. Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/weather_model.pkl")

print("Model saved to models/weather_model.pkl")
