"""
This is a boilerplate pipeline 'model_making'
generated using Kedro 0.18.3
"""
import pandas as pd
import logging
from pandas import DataFrame
from typing import Dict

log = logging.getLogger(__name__)

def prepare_data_for_models(trending_data: Dict[str, DataFrame]):
    '''Przygotowuje dane, żeby na ich podstawie utworzyć model
    
    ### Wejście:
    trending_data: słownik z dataframe'ami zawierającymi dane o filmikach na czasie
    
    ### Wyjście:
    prepared_data: ten sam słownik, ale z df'ami w formacie X i y, gdzie
        X zawiera cechy filmików na czasie, a
        y czy film, według stosunku łapek w górę do łapek w dół, jest dobry 
    '''

    prepared_data = {}

    for country, csv in trending_data.items():
        X = csv[["title", "channel_title", "tags", "views", "likes", "dislikes", "comment_count", "description"]]
        y = []
        for row in csv.index:
            likes = csv.loc[row, "likes"]
            dislikes = csv.loc[row, "dislikes"]
            is_good = 1 if (likes / dislikes) >= 0.5 else 0
            y.append(is_good)
            prepared_data[country] = pd.concat([X, pd.Series(y)], axis=1)

    return prepared_data



from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Sequential
from keras.layers import *

def create_models(prepared_data: Dict[str, DataFrame]):

    models = {}

    for country, df in prepared_data.items():
        X_train, X_test, y_train, y_test = train_test_split(df[:,-1], df[-1], test_size=0.2)
        model = Sequential([
            Input(X_train),
        ])
        models[country] = model

    return models