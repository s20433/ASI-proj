"""
This is a boilerplate pipeline 'model_making'
generated using Kedro 0.18.3
"""
import pandas as pd
import logging
from pandas import DataFrame
from typing import Dict


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