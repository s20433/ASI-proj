"""
This is a boilerplate pipeline 'pycaret'
generated using Kedro 0.18.3
"""

import pycaret
import optuna
from pycaret.classification import setup
from pycaret.classification import tune_model

def get_best_models(prepared_data, trial):
    best_models = {}

    for country, csv in prepared_data.items():
        model_setup = setup(
            data=csv,
            target="good_video",
            session_id=2137069,
            use_gpu=True
        )
        best_model = model_setup.compare_models()
        best_models[country] = tune_model(
            best_model
        )

    return best_models


def objective(best_models, trial: optuna.Trial):
    n_estimators = trial.suggest_int("model_n_estimators", low=3, high=60)
    max_depth = int(trial.suggest_loguniform("model_max_depth", low=1, high=20))
    pass