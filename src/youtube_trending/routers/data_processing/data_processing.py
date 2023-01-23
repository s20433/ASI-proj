from typing import Any, Dict, List
import random

from youtube_trending.dependencies import create_data_full_pipeline

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.runner import SequentialRunner

router = APIRouter()

@router.put("/")
def process_data(pipeline: Pipeline = Depends(create_data_full_pipeline)) -> dict[str, Any]:
    runner = SequentialRunner()
    catalog = DataCatalog(feed_dict={'params:datasets_path': "data/01_raw"})
    the_data = runner.run(pipeline=pipeline, catalog=catalog).get("prepared_data")
    random_key = random.choice(list(the_data.keys()))
    random_value = the_data.get(random_key).sample()
    return {str(random_key): str(random_value)}

#
