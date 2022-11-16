<h3>Yardage Predictor</h3>

Big data is becoming a big part of our world and sports are no execption. Teams are increasingly using advanced analytics to find an edge over their competition.

On such example of this is using modeling to find out what metrics are most predictive of future success. For example, what are the elements of wide receiver play in the NFL that are most important?

Problem to be solved: Do past receiving yards do a good job of predicting future receiving yards or are there other metrics that can do a better job?

##Key Metrics

Receiving yards -- how many yards a player gains
Targets -- how often the player is thrown the ball
Completed passs/completion/reception -- when a player successfully catches a target
Air Yards -- how far in the air the ball travels before the player attempts to catch the ball
aDOT -- Average depth of target, or air yards per target
Yardage after catch (YAC) -- the yardage the receiver gains after the catch
Implied team total -- how many points a player's team is projected to score in the given game; this is derived from betting markets
Methodology

Build a backwards-looking expected yardage model, based on inputs such as air yardage and field position.
Assess how this model and/or other factors predict future receiving yards.


##Data Sources

nflverse (https://nflverse.nflverse.com/)
nfl_data_py (https://github.com/cooperdff/nfl_data_py)
