# ml.py

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

def train_model():

    df = pd.read_csv('전세2023v3.csv', dtype={'법정동명': 'category', '건물용도': 'category'})

    X = df[['법정동명', '임대면적(㎡)', '건물용도']]
    y = df['보증금(만원)']


    X = pd.get_dummies(X, columns=['법정동명', '건물용도'], drop_first=False)
    cols = ['임대면적(㎡)'] + list(X.columns)


    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


    cols = list(X_train.columns)


    model = xgb.XGBRegressor(n_estimators=100, random_state=42, missing=-999)
    model.fit(X_train, y_train)

 
    y_val_pred = model.predict(X_val)
    rmse = mean_squared_error(y_val, y_val_pred, squared=False)

   
    with open('model.pkl', 'wb') as file:
        pickle.dump((model, cols), file)

    return model, rmse

train_model()