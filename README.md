Premier League Match Outcome Predictor

Project Overview:
This project is a machine learning-powered dashboard for predicting English Premier League (PL) match outcomes. 
It uses historical match data, advanced team statistics, and engineered features 
to forecast whether the home team will win or if the match will result in an away win/draw.
Disclaimer: It does require some deeper understanding of football for some of the features but they could easily be searched up on the internet for testing purposes.

- The model training code is in the 19-08 jupyter notebook whil various scrapers were implemented to get data from fbref as that was the
- easiest to scrape. The scraper functions are all in the all_time_fixtures jupyter notebook for reference

  
The dashboard is built with Streamlit and allows users to:

1. Select home and away teams from a dropdown.
2. Enter relevant match and team statistics with helpful explanations. 
- You would need to get the feature values like I explained. That can be gotten from a Google search
3. There are also tooltips in form of question marks to give more explanation on some of the features so users know what they need to look for
4. Get a prediction (Home Win or Away Win/Draw) with confidence.
5. View model evaluation plots (ROC Curve, Confusion Matrix, Feature Importance).

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

Disclaimer: It is purely for educational purposes and learning. Predictions should be taken with a pinch of salt.

Feel free to let me know if you want to customize any section or add more details!
---------------------------------------------------------------------------------------------------------------
Incoming improvements
1. Code will be added to take in user's desired club and get the various feature values based on real time data from the league which will save the user time of manually looking for the data
2. An API will be created to get the predictions outside of streamlit
3. Streamlit page will be made more interactive and user friendly with plots and easy to understand text
