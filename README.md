<h1>Yardage Predictor</h1>

Big data is becoming a big part of our world and sports are no execption. Teams are increasingly using advanced analytics to find an edge over their competition.

On such example of this is using modeling to find out what metrics are most predictive of future success. For example, what are the elements of wide receiver play in the NFL that are most important?

<b>Problem to be solved:</b> Do past receiving yards do a good job of predicting future receiving yards or are there other metrics that can do a better job?

<h2>Methodology</h2>

* Build a backwards-looking expected yardage model, based on inputs such as air yardage and field position.
* Use this model as input for a forward-looking model to predict future receiving yards.
* This model powers the following web app: https://salcacciatore-yardage-predictor-streamlit-app-4ugnic.streamlit.app/


<h2>Contents</h2>

* Yardage_predictor.ipynb -- Jupyter notebook that performs the analysis and creates the models.

* streamlit_app.py --  Python file that drives the web app.

* Trailing_week.csv and week_by_week.csv -- player-level receiving data from nflverse

* play_by_play_model.pkl -- backwards-looking model that predicts yardage on the play-py-play level

* in_season_model.pkl -- forwards-looking model that takes 3-6 games of data for a receiver and predicts their yardage total for the following game.





<h2>Findings</h2>

* Opportunity metrics (targets, air yards, etc.) are more useful to predicting future wide receiver performance than efficiency metrics (catch rate, yards after catch, etc.).


<h2>Data Sources</h2>

* nflverse (https://nflverse.nflverse.com/)
* nfl_data_py (https://github.com/cooperdff/nfl_data_py)
