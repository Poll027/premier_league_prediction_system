from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json
import pandas as pd

model = joblib.load('premier_league_predictor.pkl')
with open('feature_list.json') as f:
    feature_list = json.load(f)

app = FastAPI()

class TeamData(BaseModel):
    features: dict

class PredictionRequest(BaseModel):
    home_team_data: TeamData
    away_team_data: TeamData

@app.post("/predict")
def predict_match(request: PredictionRequest):
    home_team_data = request.home_team_data.features
    away_team_data = request.away_team_data.features

    features = {}
    for feature in feature_list:
        if feature.startswith('home_'):
            features[feature] = home_team_data[feature.replace('home_', '')]
        elif feature.startswith('away_'):
            features[feature] = away_team_data[feature.replace('away_', '')]
        else:
            features[feature] = (home_team_data.get(feature, 0) + away_team_data.get(feature, 0)) / 2

    input_df = pd.DataFrame([features])[feature_list]
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    return {
        'prediction': 'Home Win' if prediction == 1 else 'Away Win/Draw',
        'home_win_probability': float(probability[1]),
        'confidence': float(max(probability))
    }