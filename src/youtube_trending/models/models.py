from sqlalchemy import (Integer, String, Column, ForeignKey)

from sqlalchemy.orm import relationship

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    video_id: Column(String, index=True)
    title: Column(String, index=True)
    description: Column(String, index=True)
    tags: Iterable[str]
    likes: Column(Integer, index=True)
    dislikes: Column(Integer, index=True)
    views: Column(Integer, index=True)
    
    country = relationship("Country", back_populates="country")
