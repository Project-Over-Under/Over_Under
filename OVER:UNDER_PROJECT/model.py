#ds imports
import pandas as pd
import numpy as np
import os
import wrangle as wr
import explore as ex
# plotting
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (6,4)
plt.rcParams["font.size"] = 10
# splitting
from sklearn.model_selection import train_test_split
import scipy.stats as stats
# sklearn
import sklearn.preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score,confusion_matrix, plot_confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
#CATboost imports
from catboost import CatBoostClassifier
from sklearn.svm import SVC


df = pd.read_csv('prepped_data.csv')
df = df.drop(columns=['date', 'day_of_week', 'start_time','home_score',
       'home_wins', 'away_score','stadium', 'away_wins','total_scores'])
df['spread'] = abs(df['spread'])


def baseline():
   df['baseline'] = 1
   subset = df[df.baseline == 1]
   baseline_precision = (subset.baseline == subset.is_under).mean()
   print(f'baseline precision: {baseline_precision:.2%}')


'''~~~~~~~~~ MODELS ~~~~~~~~~~'''

X_train, y_train, X_validate, y_validate, X_test, y_test = ex.train_validate_test(df,'is_under')
X_train.shape, y_train.shape, X_validate.shape, y_validate.shape, X_test.shape, y_test.shape 
sc_X = StandardScaler()
X_train_scaled = sc_X.fit_transform(X_train)
X_validate_scaled = sc_X.transform(X_validate)
X_test_scaled = sc_X.transform(X_test)

### Log Reg
log = LogisticRegression()
log.fit(X_train_scaled, y_train)
log_preds = log.predict(X_train_scaled)

def log_reg():
   print(f'Accuracy-Train {round(log.score(X_train_scaled,y_train),4)}')
   print(f'Accuracy-Validate {round(log.score(X_validate_scaled,y_validate),4)}')
   print(classification_report(y_train,log_preds))
   print(classification_report(y_validate,log.predict(X_validate_scaled)))

def log_reg_test():
   print(f'Accuracy-TEST {round(log.score(X_test_scaled,y_test),4)}')
   print(classification_report(y_test,log.predict(X_test_scaled)))



svm = SVC()
svm.fit(X_train_scaled, y_train)
svm_preds = svm.predict(X_train_scaled)

def SVC_model():
    print(f'Accuracy-Train {round(svm.score(X_train_scaled,y_train),4)}')
    print(f'Accuracy-Validate {round(svm.score(X_validate_scaled,y_validate),4)}')
    print(classification_report(y_train,svm_preds))
    print(classification_report(y_validate,svm.predict(X_validate_scaled)))
#update

def rf():
   # create the Random Forest model 
   # df = df.drop(columns=['date', 'day_of_week', 'start_time','home_score',
         #'home_wins', 'away_score', 'away_wins','stadium','total_scores'])
   X_train, y_train, X_validate, y_validate, X_test, y_test = ex.train_validate_test(df,'is_under')

   rf1 = RandomForestClassifier(n_estimators=201,max_depth=5)
   # fit the model to the TRAIN dataset1
   rf1.fit(X_train, y_train)
   # use the model by calling for the predictions made via the TRAIN dataset
   rf1_preds = rf1.predict(X_train)
   pd.crosstab(rf1_preds,y_train) # a confusion matrix with ACTUALS as columns and PREDICTIONS as rows
   print(f'Accuracy-Train {round(rf1.score(X_train,y_train),4)}')
   print(f'Accuracy-Validate {round(rf1.score(X_validate,y_validate),4)}')
   print(classification_report(y_train,rf1_preds))
   print(classification_report(y_validate,rf1.predict(X_validate)))

def nb():
   #df = df.drop(columns=['date', 'day_of_week', 'start_time','home_score',
       # 'home_wins', 'away_score', 'away_wins','stadium','total_scores'])
   X_train, y_train, X_validate, y_validate, X_test, y_test = ex.train_validate_test(df,'is_under')


   nbc = GaussianNB()
   # fit the model to the TRAIN dataset1
   nbc.fit(X_train, y_train)
   # use the model by calling for the predictions made via the TRAIN dataset
   nbc_preds = nbc.predict(X_train)
   pd.crosstab(nbc_preds,y_train) # a confusion matrix with ACTUALS as columns and PREDICTIONS as rows
   print(f'Accuracy-Train {round(nbc.score(X_train,y_train),4)}')
   print(f'Accuracy-Validate {round(nbc.score(X_validate,y_validate),4)}')
   print(classification_report(y_train,nbc_preds))
   print(classification_report(y_validate,nbc.predict(X_validate)))