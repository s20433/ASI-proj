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
#!!!
#!!!
#!!!
            # Kontrowersyjne: jeśli nie ma łapek w dół, może też mieć mało wyświetleń
            # Więc ciężko stwierdzić, czy stosunek likes/0 faktycznie skutkuje dobrym filmem
            if dislikes == 0:
                is_good = 0
            else:
                # filmiki mające stosunek 
                is_good = 1 if (likes / dislikes) <= 0.57 else 0
            y.append(is_good)
        prepared_data[country] = pd.concat([X, pd.Series(y)], axis=1)

    return prepared_data


'''
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Model, Sequential
from keras.layers import *

import pycaret
from pycaret.classification import setup
from pycaret.classification import tune_model
import optuna
from optuna.integration import KerasPruningCallback

def create_models(prepared_data: Dict[str, DataFrame]) -> Dict[str, Model]:
    models = {}

    for country, df in prepared_data.items():
        model_setup = setup(data=df, target="good_video", session_id=2137069)
        best_model = model_setup.compare_models()
        models[country] = tune_model(best_model)

    return models

def objective(models, trial: optuna.Trial):
    factor = trial.suggest_int("learning-rate-factor", low=-8, high=-3)
    learning_rate = 10**factor
    optimizer = tf.keras.optimizers.Adam(
        learning_rate=learning_rate
    )
    accuracies = []
    for country, model in models.items():
        model.compile(
            optimizer=optimizer,
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )
        model.fit(

        )
    
    return accuracies
'''