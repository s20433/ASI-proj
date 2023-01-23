
from typing import Iterable

from kedro.pipeline import Pipeline

from youtube_trending.pipelines import data_processing, model_making

def create_data_pipeline() -> Iterable[Pipeline]:
    yield data_processing.create_pipeline()

def create_data_full_pipeline() -> Iterable[Pipeline]:
    yield (data_processing.create_pipeline() + model_making.create_pipeline())