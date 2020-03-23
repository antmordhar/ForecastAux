import pandas as pd
import pymongo
from pymongo import MongoClient

def captura():
    
    temperature = pd.read_csv("/tmp/workflow/Data/temperature.csv")
    humidity = pd.read_csv("/tmp/workflow/Data/humidity.csv")

    temperature= temperature[['datetime','San Francisco']]
    temperature= temperature.rename(columns={'San Francisco': 'SFTemperature'})

    humidity= humidity[['datetime','San Francisco']]
    humidity= humidity.rename(columns={'San Francisco': 'SFHumidity'})

    SF= pd.merge(temperature,humidity, on= 'datetime')
    SF= SF.dropna()

    # Making a Connection with MongoClient
    client = MongoClient("mongodb://127.0.0.1:27017")
    # database
    db = client["SanFrancisco"]
    # collection
    col= db["Forecast"]

    SF.reset_index(inplace=True)
    data_dict=SF.to_dict("records")
    col.insert_many(data_dict)

if __name__ == '__main__':
    captura()