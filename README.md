Premier League Match Outcome Predictor

Project Overview:
This project is a machine learning-powered dashboard for predicting English Premier League (PL) match outcomes. 
It uses historical match data, advanced team statistics, and engineered features 
to forecast whether the home team will win or if the match will result in an away win/draw.
Disclaimer: It does require some deeper understanding of football for some of the features but they could easily be searched up on the internet for testing purposes.

The dashboard is built with Streamlit and allows users to:

Select home and away teams from a dropdown.
Enter relevant match and team statistics with helpful explanations.
Get a prediction (Home Win or Away Win/Draw) with confidence.
View model evaluation plots (ROC Curve, Confusion Matrix, Feature Importance).

Project Structure:

project/
│
├── dashboard.py                # Main Streamlit app
├── premier_league_predictor.pkl # Trained RandomForest model
├── feature_list.json           # List of features used by the model
├── team_mapping.pkl            # Mapping of team names to integer IDs
├── master_df_final.csv         # Processed dataset used for training/evaluation
├── roc_plot.png                # ROC curve image for model evaluation
├── pl_conf_mat.png             # Confusion matrix image for model evaluation
├── feat_importance.png         # Feature importance image for model evaluation
├── requirements.txt            # Python dependencies

How to Use:
1. Online (Recommended)
Visit the public Streamlit app:
https://25-26-pl-season-predictor.streamlit.app/
2. Locally
Clone the repository:

Install dependencies:

Run the dashboard:

Features
1. Predict Match
Select home and away teams.
Enter match and team statistics (with tooltips explaining each feature).
Get a prediction:
"Team Home (TeamName) is expected to WIN"
or "Team Away (TeamName) is expected to WIN or DRAW"
See the model’s confidence in its prediction.

3. Model Evaluation
ROC Curve: Visualizes the model’s ability to distinguish between home wins and other outcomes.
Confusion Matrix: Shows correct and incorrect predictions for home wins.
Feature Importance: Ranks which features most influence the model’s predictions.

Data & Model
Data: Historical Premier League match data, engineered features (xG, possession, Elo ratings, head-to-head stats, etc.).
Model: RandomForestClassifier trained on the processed dataset.
Feature Engineering: Includes rolling averages, exponential moving averages and more. I also implemented an elo system similar to that from chess but that can be
easily calculated from the internet. Soon I'll add code to input the team's name and that will then give you the elo and other feature values to use.

License
This project is licensed under the MIT License.

Feel free to let me know if you want to customize any section or add more details!
