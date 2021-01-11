import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

path = 'database_prevencao.csv'
data = pd.read_csv(path, sep=';')

X = data.drop('grupo', axis=1)

y = data['grupo']

modelRandomForest = RandomForestClassifier()
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=13)
modelRandomForest.fit(train_X, train_y)

import pickle
pickle.dump(modelRandomForest,open("prevencao.sav", "wb"))
