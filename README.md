#  Project_Over_Under
#### Welcome to this initial exploration of NFL Game Data from the 1979 season until the most recent 2022 season!  The primary purpose of this project is to accurately predict whether the total scores of both teams will be less than or greater than a pre-established betting total. The project dataset was curated specifically for this project from https://www.pro-football-reference.com and was inspired by a dataset courtesy of https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data.  Individual game data for each NFL regular-season and plyoff game from 1979 until present was selected to highlight potential meta-game impacts on human performance factors.  Each game was then labeled as "Over" or "Under", based upon whether the total points scored by both teams exceeded a pre-determined betting total.

#### The goals of this initial exploration are as follows:
- PRIMARY: Generate actionable predictions regarding whether or not a game total score will exceed a pre-determined total.
- SECONDARY: Draw reasonable inferences regarding the characteristics of those games which featured total scores determined to be "Over", and those that did not.
- SECONDARY: Identify those features which retain the greatest importance for determining the potential for a particular NFL game to exceed a pre-established total game score.

#### OVER-ARCHING HYPOTHESIS AND ASSUMPTIONS:
- The total points scored by both teams in an NFL contest is a function of many factors.  We are initiaing this project to determine if any statistically significant correlations exists between total game score and meta-game, human-centered motivational factors such as weather conditions, peak-performance time-windows (day of week/time of day), playing surface, etc.

- Utilizing insights gained during exploration of the above factors, we will create a model to predict whether or not the total game score will exceed a pre-deteremined number for sports wagering purposes.  The intent is to create a model which can outperform a baseline model by 5%.  Each game is given its own unique, pre-determined "OVER/UNDER" line by odds makers and the model shall utilize this information to guide sports bettors towards making more informed wagers.  

- The 1979 NFL Season was chosen as the starting point for the dataset due to the availability of Over/Under wagering lines from this season onward.  While the game has transformed in many ways from 1979 to the present, this project seeks to adopt a team-agnostic, zoomed-out, bird's-eye view of the aggregation of the approx. 11,000 regular season and playoff games played during this time span.  

- The underlying assumption of this project is that the smaller-scale details (teams/players/injuries) purported as "important" by the sports wagering industry do not maintain as much significance as the sports-betting public is lead to believe.  This project seeks to treat each game as a human-performance/employee-performance measurement and determine if there is justification for holding the aforementioned assumption.

#### Project Planning:
- Plan: Questions and Hypotheses
- Acquire: Curated dataset courtesy of https://www.pro-football-reference.com.  Features indicating meta-game conditions were included and/or engineered from existing data.
- Prepare: Kept outliers after investigating their nature, missingness was a non-issue, as there were ZERO entries containing NULL values for predictors.  SKLearn StandardScaler used for scaling purposes.  Split into machine learning subsets (Train/Validate/Test).
- Explore: Univariate and multi-variate analysis, correlation matrix, 2D visualization, correlation significance testing, 2-sample T-testing for significant differences in means.
- Model: Established a baseline "Accuracy" of 50.7% using the most frequent target occurance of "UNDER".  Then with a XXXXXXXClassifier with XXXX hyperparameters set to XXXXX, established a new Accuracy floor of XX% on unseen TEST Data.
- Deliver: Please refer to this doc as well as the Final_XXXXXXXXX.ipynb file for the finished version of the presentation, in addition to each of the underlying exploratory notebooks.

#### Initial hypotheses and questions:
* What meaningful features can be leveraged to create a model that predicts whether or not an NFL game will feature teams which score above or below a pre-established betting line?  
* Can features which reflect the meta-game conditions under which the two teams in an NFL game are subject yield similar or even better results than the traditional statistics upon which most players/teams are evaluated? 
    1. What effect, if any, does Wind Speed have on the total game score and thus, the outcome of an Over/Under wager?
    2. How about "abnormal game schedules", i.e. any game NOT starting on Sunday afternoon, during the "normal" NFL weekly window?
    3. If the game is played indoors, or on grass vs. turf?
    4. Does it matter if the game is during the regular season or during the playoffs?  How important is the game to the teams?
* Can these chosen features transcend the changing nature of the game in order to allow for an "apples-to-apples" categorization of teams from multiple eras of NFL play? 
* If all of the above are realistic and possible, can a well-informed sports wager be placed utilizing the outputs of said modeling?
* Can the sports-wagering industry stakeholders utilize this model as part of a larger software suite to ascertain the anticipated level of "interest" in a particular wager when the Over-Under Line is set at various levels?  Could this information lead to better decisions made by odds makers, and thus, a greater ROI?

