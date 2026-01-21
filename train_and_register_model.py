import hopsworks
import joblib
from sklearn.linear_model import LinearRegression

# Login
project = hopsworks.login()
fs = project.get_feature_store()

# Get Feature View
fv = fs.get_feature_view(
    name="wah_weather_fv",
    version=1
)

# Load training data (FIX IS HERE)
X_train, X_test, y_train, y_test = fv.get_train_test_split(
    training_dataset_version=1
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "wah_weather_model.pkl")

# Register model
mr = project.get_model_registry()
weather_model = mr.python.create_model(
    name="wah_weather_model",
    description="Temperature prediction model for Wah Cantt"
)

weather_model.save("wah_weather_model.pkl")

print("✅ Model trained and registered successfully")
