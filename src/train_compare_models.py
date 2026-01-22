import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("data/wah_weather_5_months.csv")

X = df[["humidity", "pressure", "wind_speed"]]
y = df["temperature"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

results = {}

# 1️⃣ Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
results["Linear Regression"] = mean_absolute_error(y_test, lr_pred)

# 2️⃣ Decision Tree
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
results["Decision Tree"] = mean_absolute_error(y_test, dt_pred)

# 3️⃣ Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
results["Random Forest"] = mean_absolute_error(y_test, rf_pred)

# Print results
print("\nModel Comparison (Lower MAE is Better):\n")
for model, mae in results.items():
    print(f"{model}: MAE = {mae:.2f}")

# Select best model
best_model = min(results, key=results.get)
print(f"\nBest Model: {best_model}")
