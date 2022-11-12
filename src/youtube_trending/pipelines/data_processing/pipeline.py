from kedro.pipeline import Pipeline, node, pipeline

from .nodes import read_files

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
           node(
                func=read_files,
                inputs="params:datasets_path",
                outputs=["csvs", "categories"],
                name="file_reading_node",
            )            
        ]
    )
