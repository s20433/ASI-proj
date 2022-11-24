"""
This is a boilerplate pipeline 'model_making'
generated using Kedro 0.18.3
"""
import pandas as pd
import numpy as np
import logging
from pandas import DataFrame
from typing import Dict

log = logging.getLogger(__name__)

def prepare_data_for_models(trending_data: Dict[str, DataFrame]):
    '''Przygotowuje dane, żeby na ich podstawie utworzyć model
    
    ### Wejście:
    data_raw: dataframe zawierający dane o filmikach na czasie
    
    ### Wyjście:
    country_data: ten sam dataframe, ale w formacie X i y, gdzie
        X zawiera cechy filmików na czasie, a
        y czy film, według stosunku łapek w górę do łapek w dół, jest dobry 
    '''

    prepared_data = {}

    for country, df in trending_data.items():
        X = df[("title", "channel_title", "tags", "views", "likes", "dislikes", "comment_count", "description")]
        y = pd.Series()
        for row in df.index:
            likes = df.loc[row, "likes"]
            dislikes = df.loc[row, "dislikes"]
            log.info("Likes to dislikes: ", (likes/dislikes))
            y[row] = 1 if (likes / dislikes) >= 0.5 else 0
            prepared_data[country] = pd.DataFrame((X, y))

    return prepared_data