"""
This is a boilerplate pipeline 'model_making'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import prepare_data_for_model, create_models


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=create_models,
            inputs="trending_data",
            outputs="models",
            name="model_making_node",
        )
    ])
