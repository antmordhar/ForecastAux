import pandas as pd
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
import numpy as np
from sklearn.externals import joblib


def predecir(n):

    modeloTemperatura= joblib.load('./Modelos/modeloTemperatura.pkl')
    modeloHumidity= joblib.load('./Modelos/modeloHumidity.pkl')
    
    prediccionTemperatura, confint = modeloTemperatura.predict(n_periods=n, return_conf_int=True)
    prediccionHumidity, confint = modeloHumidity.predict(n_periods=n, return_conf_int=True)
    
    # todays_date = datetime.now().date()
    todays_date = datetime.now()
    index = pd.date_range(todays_date, periods=n, freq='H')

    odf= pd.DataFrame(index=index, columns=['temperatura','humedad'])
    temperatura=np.array(prediccionTemperatura)
    humedad=np.array(prediccionHumidity)
    odf['temperatura']=temperatura
    odf['humedad']=humedad

    return odf