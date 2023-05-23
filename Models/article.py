from pydantic import BaseModel
from typing import (Text, Optional)
from datetime import datetime

class Article(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False
