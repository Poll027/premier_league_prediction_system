import streamlit as st
import joblib
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve, auc

model = joblib.load('project/premier_league_predictor.pkl')
with open('project/feature_list.json') as f:
    feature_list = json.load(f)
mapping_dict = joblib.load('project/team_mapping.pkl')
master_df = pd.read_csv('project/master_df_final.csv')

ID_TEAM_MAP = {v: k for k, v in mapping_dict.items()}
teams = list(mapping_dict.keys())

st.set_page_config(page_title="PL Predictor", layout="wide")
st.title("Premier League Match Predictor")

page = st.sidebar.selectbox("Select Page", ["Predict Match", "Model Evaluation", "Feature Correlation"])

if page == "Predict Match":
    feature_explanations = {
    'xG': 'Expected goals (xG): Estimate of goals based on shot quality.',
    'Sh': 'Shots: Total number of shots taken.',
    'Tkl': 'Tackles: Number of tackles made.',
    'Poss': 'Possession (%): Average possession percentage.',
    'days_rest': 'Days Rest: Days since last match.',
    'form_last5': 'Form (last 5): Win rate in last 5 matches (0-1).',
    'xG_ema10': 'xG (EMA10): 10-match exponential moving average of xG.',
    'Poss_ema10': 'Possession (EMA10): 10-match moving average.',
    'Tkl_ema10': 'Tackles (EMA10): 10-match moving average.',
    'h2h_goal_avg': 'Head-to-head avg goals: Avg goals in recent meetings.',
    'h2h_win_pct': 'Head-to-head win %: Win rate in recent meetings.',
    'h2h_recent_trend': 'Head-to-head trend: Result of last meeting (1=win, 0=draw, -1=loss).',
    'h2h_venue_impact': 'Venue impact: Difference in win % at home vs away.',
    'danger_ratio': 'Danger ratio: Shots per opposition tackle.',
    'poss_eff': 'Possession efficiency: xG per possession.',
    'elo': 'Elo rating: Team strength score.',
    'elo_momentum': 'Elo momentum: Recent Elo change.',
    'elo_advantage': 'Elo advantage: Home Elo / Away Elo.',
    'elo_trend': 'Elo trend: Recent Elo change / current Elo.'
    }
    st.header("Predict a Match Outcome")
    col1, col2 = st.columns(2)
    with col1:
        home_team = st.selectbox("Select Home Team", teams)
    with col2:
        away_team = st.selectbox("Select Away Team", [t for t in teams if t != home_team])

    home_id = mapping_dict[home_team]
    away_id = mapping_dict[away_team]

    st.markdown("Enter Feature Data")
    home_features = {}
    away_features = {}

    for feature in feature_list:
        if feature.startswith('home_'):
            f = feature.replace('home_', '')
            home_features[f] = st.number_input(
                f"Home {f}", value=0.0, key=f"home_{f}", help=feature_explanations.get(f, '')
            )
        elif feature.startswith('away_'):
            f = feature.replace('away_', '')
            away_features[f] = st.number_input(
                f"Away {f}", value=0.0, key=f"away_{f}", help=feature_explanations.get(f, '')
            )

    for feature in feature_list:
        if not feature.startswith('home_') and not feature.startswith('away_'):
            val = st.number_input(
                f"{feature} (average for both teams)", value=0.0, key=feature, help=feature_explanations.get(feature, '')
            )
            home_features[feature] = val
            away_features[feature] = val

    if st.button("Predict"):
        
        features = {}
        for feature in feature_list:
            if feature.startswith('home_'):
                features[feature] = home_features.get(feature.replace('home_', ''), 0)
            elif feature.startswith('away_'):
                features[feature] = away_features.get(feature.replace('away_', ''), 0)
            else:
                features[feature] = (home_features.get(feature, 0) + away_features.get(feature, 0)) / 2


        for feature in feature_list:
            if feature not in features:
                features[feature] = 0

        input_df = pd.DataFrame([features], columns=feature_list)
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]
        confidence = float(max(probability))
        result = f"Team Away ({away_team}) is expected to NOT WIN"
        if prediction == 1:
            result = f"Team Home ({home_team}) is expected to WIN"
            prob = probability[1]
        else:
            result = f"Team Away ({away_team}) is expected to WIN or DRAW"
            prob = probability[0]

        st.success(result)
        st.write(f"Confidence: {confidence:.2f}")

elif page == "Model Evaluation":
    st.header("Model Evaluation")

    st.subheader("ROC Curve")
    st.image("project/roc_plot.png", use_column_width=True)
    st.markdown(
        "The ROC Curve shows how well the model distinguishes between home wins and other outcomes. "
        "A curve closer to the top-left means better performance. The area under the curve (AUC) is a summary of this ability."
    )

    st.subheader("Confusion Matrix")
    st.image("project/pl_conf_mat.png", use_column_width=True)
    st.markdown(
        "The Confusion Matrix shows how many matches were correctly or incorrectly predicted as home wins or not. "
        "It helps you see where the model makes mistakes and where it gets things right."
    )

    st.subheader("Feature Importance")
    st.image("project/feat_importance.png", use_column_width=True)
    st.markdown(
        "This plot ranks the features by how much they influence the model's predictions. "
        "Features at the top are the most important for deciding match outcomes."
    )