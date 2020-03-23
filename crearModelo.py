import pandas as pd
import pymongo
from pymongo import MongoClient
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
from sklearn.externals import joblib

def crearModelo():

    client = MongoClient("mongodb://0.0.0.0:27017")
    db = client["SanFrancisco"]
    col= db["Forecast"]
    df = pd.DataFrame(list(col.find()))
    df=df[['datetime','SFTemperature','SFHumidity']]

    modeloTemperatura = pm.auto_arima(df[['SFTemperature']], start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)
    
    joblib.dump(modeloTemperatura, './Modelos/modeloTemperatura.pkl')

    modeloHumidity = pm.auto_arima(df[['SFHumidity']], start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)

    joblib.dump(modeloHumidity, './Modelos/modeloHumidity.pkl')

if __name__ == '__main__':
    crearModelo()