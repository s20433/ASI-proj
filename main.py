from enum import Enum
from typing import Iterable
from kedro.pipeline import Pipeline

from fastapi import FastAPI, Query, Path, Body, Depends
from pydantic import BaseModel, Field

from youtube_trending.pipelines.data_processing import create_pipeline

app = FastAPI()

class MyResult(BaseModel):
	hello: str

def create_data_pipeline() -> Iterable[Pipeline]:
	yield create_pipeline()

@app.get('/')
def main(pipeline: Pipeline = Depends(create_data_pipeline)) -> MyResult:
	return MyResult(hello="ASI")
