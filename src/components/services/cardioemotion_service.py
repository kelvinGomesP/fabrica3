from sqlalchemy.orm import Session
from src.components.models.cardioemotion import CardioEmotion

def create_cardioemotion(db: Session, cardioemotion_data):
    nova_cardioemotion = CardioEmotion(**cardioemotion_data)
    db.add(nova_cardioemotion)
    db.commit()
    db.refresh(nova_cardioemotion)
    return nova_cardioemotion

def get_cardioemotions(db: Session):
    return db.query(CardioEmotion).all()
