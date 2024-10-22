from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.components.models.db import get_db
from src.components.services.cardioemotion_service import create_cardioemotion, get_cardioemotions

# Definir o esquema Pydantic para validação de entrada
class CardioEmotionCreate(BaseModel):
    id_instrumento: int
    session_datetime: str
    green_percent: float = None
    blue_percent: float = None
    red_percent: float = None
    bpm_avg: int = None
    data1: str = None

router = APIRouter()

# Rota para criar uma nova medição de CardioEmotion
@router.post("/cardioemotions/")
def criar_cardioemotion(cardioemotion: CardioEmotionCreate, db: Session = Depends(get_db)):
    cardioemotion_data = cardioemotion.dict()
    return create_cardioemotion(db, cardioemotion_data)

# Rota para listar todas as medições de CardioEmotion
@router.get("/cardioemotions/")
def listar_cardioemotions(db: Session = Depends(get_db)):
    return get_cardioemotions(db)
