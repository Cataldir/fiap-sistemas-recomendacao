from typing import Dict, List

from pydantic import BaseModel


class UserProfile(BaseModel):
    user_id: int
    name: str
    age: int
    gender: str
    profession: str


class UserInteractions(BaseModel):
    user_id: int
    interactions: Dict[int, int]
