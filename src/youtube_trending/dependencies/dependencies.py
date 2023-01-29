from typing import Iterable
from os import system
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline

from youtube_trending.pipelines import data_processing, model_making

def get_data() -> Iterable[DataCatalog]:
    # TODO jak tu przepchnąć dvc pull?
    return DataCatalog(feed_dict={'params:datasets_path': "data/01_raw"})

def create_data_pipeline() -> Iterable[Pipeline]:
    yield data_processing.create_pipeline()

def create_data_full_pipeline() -> Iterable[Pipeline]:
    yield (data_processing.create_pipeline() + model_making.create_pipeline())