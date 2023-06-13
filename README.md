<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

#  Project_Over_Under
#### Welcome to this initial exploration of NFL Game Data from the 1979 season until the most current 2022 season!  The primary purpose of this project is to accurately predict whether the total scores of both teams will be less than or greater than a pre-established betting total. The project dataset was curated specifically for this project from https://www.pro-football-reference.com and was inspired by a dataset courtesy of https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data.  Individual game data for each NFL regular-season and plyoff game from 1979 until present was selected to highlight potential meta-game impacts on human performance factors.  Each game was then labeled as "Over" or "Under", based upon whether the total points scored by both teams exceeded a pre-determined betting total.

<!-- TABLE OF CONTENTS -->
<details open>
  <summary style="font-size: 30px">Table of Contents</summary>
  <ol>
    <li>
      <a href="#background">Background and Planning</a>
    </li>
    <li>
      <a href="#Exploration">Exploration</a>
    </li>
    <li>
      <a href="#Data">Data</a>
    </li>
    <li><a href="#Findings, Takeaways and Recommendations">Findings, Takewaways and Recommendations</a></li>
    <li><a href="#application">Application</a></li>
    <li><a href="#reproduce">Reproduce Our Work</a></li>
  </ol>
</details>

<!-- HEADER EXAMPLES -->
## Background and Planning

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
- Explore: Univariate and multi-variate analysis, correlation matrix, 2D visualization, 2-sample T-testing for significant differences in means, chi$^2$ testing for discrete distributions.
- Model: Established a baseline "PRECISION" of 50.7% using the most frequent target occurance of "UNDER".  Then with an "out-of-the-box" LogisticClassifier with default hyperparameters, established a new PRECISION floor of 52.6% on unseen VALIDATION Data.  Testing was completed using this algorithm to achieve a PRECISION
- Deliver: Please refer to this doc as well as the Over:Under.ipynb file for the finished version of the presentation, in addition to each of the underlying exploratory notebooks.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- HEADER EXAMPLES -->
## Exploration
#### Initial hypotheses and questions:
* What meaningful features can be leveraged to create a model that predicts whether or not an NFL game will feature teams which score above or below a pre-established betting line?  
* Can features which reflect the meta-game conditions under which the two teams in an NFL game are subject yield similar or even better results than the traditional statistics upon which most players/teams are evaluated? 
    1. What effect, if any, does Wind Speed have on the total game score and thus, the outcome of an Over/Under wager?
    2. How about "abnormal game schedules", i.e. any game NOT starting on Sunday afternoon, during the "normal" NFL weekly window?
    3. If the game is played indoors, or on grass vs. turf?
    4. Does it matter if the game is during the regular season or during the playoffs?  How important is the game to the teams?
* Can these chosen features transcend the changing nature of the game in order to allow for an "apples-to-apples" categorization of teams from multiple eras of NFL play? 
* If all of the above are realistic and possible, can a well-informed sports wager be placed utilizing the outputs of said modeling?
* Can sports-wagering industry stakeholders utilize this model as part of a larger software suite to ascertain the anticipated level of "interest" in a particular wager when the Over-Under Line is set at various levels?  Could this information lead to better decisions made by odds makers, and therefore, greater ROI potentials?
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- HEADER EXAMPLES -->
## Data 

|Feature |  Data type | Definition |
|---|---|---|
| date: | datetime | Day-Month-Year|
| day_of_week: | int  | Day of the week when the game begins |
| start_times: | int  | Hour of the day when the game begins |
| week_num: | int  | Week number for the game during the season |
| home_score: | int | Final score for home team |
| home_wins: | int | Total home team wins before game start |
| stadium: | str | Statium where the game was played |
| away_score: | int  | Final score for away team |
| away_wins: | int  | Total home team wins before game start  |
| temp: | int  | Temperature during the game |
| humidity: | int  | Humidity during the game |
| wind: | int  | Wind during the game |
| spread: | float | Spead of the game (How likely a team will win) |
| ou: | float | Over/Under betting score set by Professionals/Vegas | 
| is_under: | bool  | TARGET: Is the game ou score over or under the Vegas Score |
| abnormal_start: | bool | Does the game have a non-Sunday Afternoon start|
| total_scores : | int | Total scores combined for home and away teams|
| playoff_implications: | bool | Does the game have playoff implications |
| is_turf: | bool  | Does the field use grass or turf-variant |
| is_outdoor: | bool  | Is the Game played outdoors or inside a dome |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Findings, Takeaways and Recommendations

- Modeling was optimized for PRECISION for the Positive Class ("is_under").  The nature of sports wagering allows False Negatives to be inconsequential, however, False Positives are punished significantly via loss of wagering capital.
- Baseline PRECISION for the most-common, Positive class is 50.7%.  We calculate this rate by predicting all instances to be an instance of "is_under", and then calculate the percentage of correct predictions.
- A realistic expectation for Precision on the Validation subset ranges between 49% and 53%.  Tree-Based models performed admirably well, as did the Gaussian and Bernoulli Naive-Bayes variants.  A Multiple LogisticRegression classifier peformed the best and was chosen as the model for Testing purposes.  Multiple Logistic Regression models also provided coefficient information for determining feature importance.
- This implies that not only is it possible to achieve a marginal "predictive capability", but we may also retain a realistic level of "interpretability" or explainability with our results if we were to use Tree-Based classifiers.
- Along with DecisionTree and Random Forest models, LogRegression pointed towards the features "wind" (wind speed) and "ou" (over/under betting line) as the Top 2 features.
- While our model is currently able to outperform baseline PRECISION for the positive class by over 2%, these results do not yet allow for an informed sports wager to be made with POSITIVE EXPECTED VALUE.  A PRECISION value of greater than 55% is needed for this to be the case.
- In the future, it is recommended to further explore applications of ML clustering on this dataset to support an increase in the predictive power of classification models.  Additionally, introducing new features into the dataset may improve model performance.  Finally, performance gains may be achieved by utilizing a subset of dataset features.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Applications:

- For the purposes of placing "Over/Under" wagers for NFL games, the first step is to decide upon a wagering strategy.  Do we look to maximize the ACCURACY of bets regardless of whether we bet "Over" or "Under", or is it wiser to identify (PRECISION) those games which are predicted to be "Under", and thus limit ourselves to betting the "Under" on these games?
- For oddsmakers who are responsible for setting the Over/Under betting lines which will garner the most interest (and thus profits) from the sports-wagering public, this model would compliment existing software tools by providing insights into the corrsponding probabilities of "Over" and "Under" for each possible value of the "Over/Under" line.  That number which is closest to a 50/50 split would indicate the number which will generate the greatest Return on Investment (ROI).
- Further evaluation is necessary to compare the probability that the total score in an NFL game is over or under a particular betting line to the payoff odds offered by the sportsbook.  Much information is publicly available to make this evaluation so that a wager can be made with a Positive Expected Value.  It is outside the scope of this project to elaborate further on the topic of sports wagering theory and practice.  As a starting point, please visit the "Wizard of Odds", Michael Shackleford's website at https://wizardofodds.com/games/sports-betting.

#### Instructions for those who wish to reproduce this work or simply follow along:
You Will Need (ALL files must be placed in THE SAME FOLDER!):
- 1. Over:Under.ipynb file from the OVER:UNDER_PROJECT folder in this git repo
- 2. wrangle.py file from the OVER:UNDER_PROJECT folder in this git repo
- 3. explore.py file from the OVER:UNDER_PROJECT folder in this git repo
- 4. model.py file from the OVER:UNDER_PROJECT folder in this git repo
- 5. XXXXXXXXX.csv located at : XXXXXXwww.somesite.comXXXXXXXX

Ensure:
- CATBoost library required in the working environment, however, the code in the Over:Under.ipynb file can be removed or commented out in order to run the notebook.
- XGBoost library required in the working environment, however, the code in the Over:Under.ipynb file can be removed or commented out in order to run the notebook.
- All files are in the SAME FOLDER
- wrangle.py, explore.py and model.py each have the .py extension in the file name

Any further assistance required, please email me at myemail@somecompany.com.
