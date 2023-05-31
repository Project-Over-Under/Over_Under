#  Project_Over_Under
#### Welcome to this initial exploration of NFL Contest Data from the 1979-80 season until the current 2022-23 season!  The primary purpose of this project is to accurately predict whether the total scores of both teams will be less than or greater than a pre-established total. The project data-set was curated specifically for this project and is based upon data courtesy of https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data.  Additional data was acquired from https://www.pro-football-reference.com.  Individual-game data for each NFL regular-season and plyoff game from 1979 until present was selected to highlight potential meta-game impacts on human-performance factors.  Each game was then labeled as "Over" or "Under", based upon whether the total points scored by both teams exceeded a pre-determined betting total.

#### The goals of this initial exploration are as follows:
- PRIMARY: Generate actionable predictions regarding whether or not a game total score will exceed a pre-determined total.
- SECONDARY: Draw reasonable inferences regarding the characteristics of those games which featured total scores determined to be "Over", and those that did not.
- SECONDARY: Identify those features which retain the greatest importance for determining the potential for a particular NFL game to exceed a pre-established total game score.

#### OVER-ARCHING HYPOTHESIS AND ASSUMPTIONS:
- The total points scored by both teams in an NFL contest is a function of many factors.  We are initiaing this project to determine if any statistically significant correlations exists between total game score and meta-game, human-centered motivational factors such as weather conditions, peak-performance time-windows (day of week/time of day), playing surface, etc.

- Utilizing insights gained during exploration of the above factors, we will create a model to predict whether or not the total game score will exceed a pre-deteremined number for sports wagering purposes.  The intent is to create a model which can outperform a baseline model by XXXXXXXXXXXX.  Each game is given its own unique pre-determined "OVER/UNDER" line by odds makers in various sportsbooks worldwide and the model shall guide sports bettors towards making more informed wagers and less spurious wagers.  

- The 1979 NFL Season was chosen as the starting point for the dataset due to the availability of Over/Under wagering lines from this season onward.  While the game has transformed in many ways from 1979 to the present, this project seeks to adopt a team-agnostic, zoomed-out, bird's-eye view of the aggregation of the approx. 11,000 regular season and playoff games played during this time span.  

- The underlying assumption of this project is that the smaller-scale details (teams/players/injuries) proported by the sports wagering industry do not maintain as much significance as the sports-betting public is lead to believe.  This project seeks to treat each game as a human-performance/employee-performance measurement and determine if there is justification for holding the aforementioned assumption.

#### Project Planning:
- Plan: Questions and Hypotheses
- Acquire: Curated dataset courtesy of https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data and https://www.pro-football-reference.com.  Features indicating meta-game conditions were included and/or engineered from existing data.
- Prepare: Kept outliers after investigating their nature, missingness was a non-issue, as there were ZERO entries containing NULL values for predictors.  SKLearn StandardScaler used for scaling purposes.  Split into machine learning subsets (Train/Validate/Test).
- Explore: Univariate and multi-variate analysis, correlation matrix, 2D visualization, correlation significance testing, 2-sample T-testing for significant differences in means.
- Model: Established a baseline "Accuracy" of 5X.X% using the most frequent target occurance of "UNDER".  Then with a DecisionTreeClassifier with MaxDepth set to 4, established a new Accuracy floor of XX%.
- Deliver: Please refer to this doc as well as the Final_XXXXXXXXX.ipynb file for the finished version of the presentation, in addition to each of the underlying exploratory notebooks.