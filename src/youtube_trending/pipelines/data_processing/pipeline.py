from kedro.pipeline import Pipeline, node, pipeline

from .nodes import read_files, prepare_trending_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=read_files,
                inputs="params:datasets_path",
                outputs=["csvs", "categories"],
                name="file_reading_node",
            ),
            node(
                func=prepare_trending_data,
                inputs=["csvs", "categories"],
                outputs="trending_data",
                name="data_processing_node"
            )
        ]
    )