from sqlalchemy.orm import Session
from src.components.models.vr import VR

def create_vr(db: Session, vr_data):
    novo_vr = VR(**vr_data)
    db.add(novo_vr)
    db.commit()  # Persistindo no banco
    db.refresh(novo_vr)
    return novo_vr

def get_vr(db: Session):
    return db.query(VR).all()
