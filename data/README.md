# AQI Weather Prediction – Wah Cantt, Pakistan

## Project Overview
This project implements an end-to-end MLOps pipeline to predict the next 3 days' temperature for Wah Cantt, Pakistan using live weather data.

## Features
- Weather data fetched via API (no CSV usage)
- Multiple ML models trained and compared
- Best model selected automatically
- Model metadata stored in MongoDB Atlas
- CI/CD pipeline using GitHub Actions
- Live weather based 3-day prediction

## Data Source
- Open-Meteo API (historical + live weather)

## Models Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## CI/CD
- Automated training & evaluation on each push
- Metadata stored securely using GitHub Secrets

## Location
Wah Cantt, Pakistan

## How to Run Locally
```bash
pip install -r requirements.txt
python src/train_compare_models.py
python src/predict_next_3_days.py
