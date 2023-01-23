from fastapi import FastAPI
from youtube_trending.routers import data_processing

app = FastAPI(title="YouTube Trending Browser", version="pre-0.0.1")

app.include_router(data_processing.router)

