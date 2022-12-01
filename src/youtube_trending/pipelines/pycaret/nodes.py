"""
This is a boilerplate pipeline 'pycaret'
generated using Kedro 0.18.3
"""

import pycaret
from pycaret.classification import setup
from pycaret.classification import tune_model

def get_best_models(prepared_data):
    best_models = {}

    for country, csv in prepared_data.items():
        model_setup = setup(data=csv, target="good_video", session_id=2137069)
        best_model = model_setup.compare_models()
        best_models[country] = tune_model(best_model)

    return best_models

