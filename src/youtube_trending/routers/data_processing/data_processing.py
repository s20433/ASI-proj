from typing import Any, Dict, List
import random

from youtube_trending.dependencies import create_data_full_pipeline, get_data

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.runner import SequentialRunner

router = APIRouter()

@router.get("/")
def process_data(
    catalog: DataCatalog = Depends(get_data),
    pipeline: Pipeline = Depends(create_data_full_pipeline),
    country_code: str = "") -> dict[str, Any]:

    runner = SequentialRunner()
    the_data = runner.run(pipeline=pipeline, catalog=catalog).get("prepared_data")
    key = ""
    if country_code == "":
        key = random.choice(list(the_data.keys()))
    else:
        key = country_code
    random_value = the_data.get(key).sample()
    return {"random video trending in: "+str(key): str(random_value)}


