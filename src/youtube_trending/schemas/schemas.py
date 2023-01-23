from pydantic import BaseModel, Field
from typing import Iterable, List

#video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description

class VideoBase(BaseModel):
    video_id: str
    trending_date: str
    title: str
    channel_title: str
    category_id: int
    publish_time: str
    views: int
    likes: int
    dislikes: int
    comment_count: int

class VideoCreate(VideoBase):
    pass

    class Config:
        frozen = True

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True