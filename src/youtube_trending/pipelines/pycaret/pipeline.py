"""
This is a boilerplate pipeline 'pycaret'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_best_models


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=get_best_models,
            inputs=["prepared_data", "trial"],
            outputs="models",
            name="pycaret_model_picker_node"
        )
    ])
