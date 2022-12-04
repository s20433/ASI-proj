"""
This is a boilerplate pipeline 'model_making'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import prepare_data_for_models, create_models, tune_model_parameters


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=prepare_data_for_models,
            inputs="trending_data",
            outputs="prepared_data",
            name="data_preparing_node",
        ),
        node(
            func=create_models,
            inputs="prepared_data",
            outputs="models",
            name="pycaret_model_finder_node"
        )#,
        #node(
        #    func=tune_model_parameters,
        #    inputs=["models", "params:optuna_trial"],
        #    outputs="tuned_models",
        #    name="optuna_model_tuning_node"
        #)
    ])
