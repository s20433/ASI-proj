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

            # Kontrowersyjne: jeśli nie ma łapek w dół, może też mieć mało wyświetleń
            # Więc ciężko stwierdzić, czy stosunek likes/0 faktycznie skutkuje dobrym filmem
            if dislikes == 0:
                is_good = 0
            else:
                # filmiki mające stosunek 
                is_good = 1 if (likes / (likes+dislikes)) >= 0.69 else 0
            y.append(is_good)
        prepared_data[country] = pd.concat([X, pd.Series(y, name="good_video")], axis=1)
    return prepared_data

import wandb
from pycaret.classification import setup
from pycaret.classification import tune_model
from functools import partial

def create_models(prepared_data: Dict[str, DataFrame]):
    '''Wykorzystuje przygotowane dane, żeby za pomocą PyCareta wybrać najlepszy
    model dla każdego dataframe'a

    ### Wejście:
    prepared_data: ten sam słownik, ale z df'ami w formacie X i y, gdzie
        X zawiera cechy filmików na czasie, a
        y czy film, według stosunku łapek w górę do łapek w dół, jest dobry 
    
    ### Wyjście:
    models: słownik, gdzie kluczem jest nazwa kraju, a wartością wybrany przez PyCareta model
    '''
    models = {}

    run = wandb.init(project="youtube_trending_tracking")

    for country, df in prepared_data.items():
        model_setup = setup(
            data=df,
            target="good_video",
            log_experiment=True,
            experiment_name="youtube_trending_tracking",
            session_id=2137069,
            verbose=False
        )
        models[country] = model_setup.compare_models(
            include=["dt", "gbc", "ada", "rf", "et", "ridge", "knn"]
        )
    run.finish()
    return models

import optuna
from optuna import Trial

def objective(trial: Trial, models):
    _tune_model_parameters(models, trial)
    pass


def _tune_model_parameters(models, optuna_trial: Trial):
    '''Dostraja modele wykorzystując parametry zasugerowane przez Optunę
    
    ### Wejście:
    models: słownik, gdzie kluczem jest nazwa kraju, a wartością wybrany przez PyCareta model
    optuna_trial: Wstrzyknięty z zewnątrz trial Optuny, żeby wykonywać sugestie

    ### Wyjście:
    tuned_models: ten sam słownik, tylko z dostrojonymi modelami
    '''
    tuned_models = {}

    for country, model in models.items():
        tuned_model = tune_model(model,
            round=optuna_trial.suggest_int(f"{country}-tuner-round", low=3, high=6),
            n_iter=optuna_trial.suggest_int(f"{country}-tuner-iters", low=5, high=50),
        )
        tuned_models[country] = tuned_model
    
    return tuned_models

def tune_model_parameters(models):
    '''Uruchamia Optunę
    
    ### Wejście:
    models: słownik, gdzie kluczem jest nazwa kraju, a wartością wybrany przez PyCareta model
    '''
    study = optuna.create_study(
        storage="sqlite:///yt-trending-trials.db",
        sampler=optuna.samplers.NSGAIISampler(),
        pruner=optuna.pruners.SuccessiveHalvingPruner(),
        study_name="yt-trending-study",
        direction=optuna.study.StudyDirection.MAXIMIZE,
        load_if_exists=True
    )
    study.optimize(func=partial(objective, models=models), n_trials=10, n_jobs=1, show_progress_bar=True)

