# src/components/services/cardioemotion_service.py
from pydantic import BaseModel
from typing import Optional

class CardioEmotionBase(BaseModel):
    Id_instrumento: int
    Session_datetime: str
    Green_percent: Optional[float] = None
    Blue_percent: Optional[float] = None
    Red_percent: Optional[float] = None
    Bpm_avg: Optional[int] = None
    Data1: Optional[str] = None

class CardioEmotionCreate(CardioEmotionBase):
    pass

class CardioEmotion(CardioEmotionBase):
    Id_CardioEmotion: int

    class Config:
        orm_mode = True
