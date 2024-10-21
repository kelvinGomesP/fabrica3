# src/routers/cardioemotion.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.components.models.db import get_db
from src.components.models.cardioemotion import CardioEmotion as CardioEmotionModel
from src.components.services.cardioemotion_service import CardioEmotionCreate, CardioEmotion  # Corrigido para importar do service

router = APIRouter()

@router.post("/cardioemotion/", response_model=CardioEmotion)
def create_cardioemotion(cardioemotion: CardioEmotionCreate, db: Session = Depends(get_db)):
    db_cardioemotion = CardioEmotionModel(**cardioemotion.dict())
    db.add(db_cardioemotion)
    db.commit()
    db.refresh(db_cardioemotion)
    return db_cardioemotion

@router.get("/cardioemotion/{cardioemotion_id}", response_model=CardioEmotion)
def read_cardioemotion(cardioemotion_id: int, db: Session = Depends(get_db)):
    db_cardioemotion = db.query(CardioEmotionModel).filter(CardioEmotionModel.Id_CardioEmotion == cardioemotion_id).first()
    if db_cardioemotion is None:
        raise HTTPException(status_code=404, detail="CardioEmotion not found")
    return db_cardioemotion

@router.put("/cardioemotion/{cardioemotion_id}", response_model=CardioEmotion)
def update_cardioemotion(cardioemotion_id: int, cardioemotion: CardioEmotionCreate, db: Session = Depends(get_db)):
    db_cardioemotion = db.query(CardioEmotionModel).filter(CardioEmotionModel.Id_CardioEmotion == cardioemotion_id).first()
    if db_cardioemotion is None:
        raise HTTPException(status_code=404, detail="CardioEmotion not found")
    for key, value in cardioemotion.dict().items():
        setattr(db_cardioemotion, key, value)
    db.commit()
    db.refresh(db_cardioemotion)
    return db_cardioemotion

@router.delete("/cardioemotion/{cardioemotion_id}", response_model=CardioEmotion)
def delete_cardioemotion(cardioemotion_id: int, db: Session = Depends(get_db)):
    db_cardioemotion = db.query(CardioEmotionModel).filter(CardioEmotionModel.Id_CardioEmotion == cardioemotion_id).first()
    if db_cardioemotion is None:
        raise HTTPException(status_code=404, detail="CardioEmotion not found")
    db.delete(db_cardioemotion)
    db.commit()
    return db_cardioemotion
