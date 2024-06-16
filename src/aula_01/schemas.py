from typing import Optional, List

from pydantic import BaseModel


class ItemClick(BaseModel):
    item_id: str
    timestamp: float


class Item(BaseModel):
    id: str
    name: str
    price: float
    clicks: Optional[List[ItemClick]] = None
    sentiment_scores: Optional[List[int]] = None
    description: Optional[str] = None
