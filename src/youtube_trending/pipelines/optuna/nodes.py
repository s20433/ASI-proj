"""
This is a boilerplate pipeline 'optuna'
generated using Kedro 0.18.3
"""

from typing import Dict
from pandas import DataFrame
import optuna


''' zróbcie coś z tym, ja nie wiem co
*(
    tf.keras.layers.Dense(
        trial.suggest_int(name=f"dense-neurons-{i}", low=8, high=16),
        activation=trial.suggest_categorical(name="dense-activation-{i}", choices=["relu", "linear"])
    )
    for i in range(trial.suggest_int(name="dense-count", low=1, high=4))
'''


def get_parameters(prepared_data: Dict[str, DataFrame], trial: optuna.Trial):
    parameters = {}

    pass