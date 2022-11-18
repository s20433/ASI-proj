"""
This is a boilerplate pipeline 'model_making'
generated using Kedro 0.18.3
"""
import pandas as pd
import numpy as np
import logging
from pandas import DataFrame
from typing import Dict

def prepare_data_for_models(data_raw):
    '''Przygotowuje dane, żeby na ich podstawie utworzyć model
    
    ### Wejście:
    data_raw: dataframe zawierający dane o filmikach na czasie
    
    ### Wyjście:
    country_data: ten sam dataframe, ale w formacie X i y, gdzie
        X zawiera cechy filmików na czasie, a
        y 
    '''
    pass

def create_models(trending_data: Dict[str, DataFrame]):
    '''Tworzy kilka modeli na podstawie słownika dataframe'ów
    
    ### Wejście:
    trending_data: słownik gdzie kluczem jest nazwa pliku, a wartością dobrze przygotowany dataframe

    ### Wyjście:
    models: słownik gdzie kluczem jest nazwa pliku, a wartością stworzony model
    '''

    models = {}

    for country, df in trending_data.items():
        models[country] = prepare_data_for_models(df)

    return models