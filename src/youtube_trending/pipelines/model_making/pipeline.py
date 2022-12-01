"""
This is a boilerplate pipeline 'model_making'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import prepare_data_for_models, create_models


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=prepare_data_for_models,
            inputs="trending_data",
            outputs="prepared_data",
            name="model_making_node",
        )
    ])
