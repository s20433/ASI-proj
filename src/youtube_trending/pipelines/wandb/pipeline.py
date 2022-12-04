"""
This is a boilerplate pipeline 'wandb'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import run_wandb

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=run_wandb,
            inputs="models, params:n_estimators, params:max_depth",
            outputs="",
            name="wandb_node"
        )
    ])
