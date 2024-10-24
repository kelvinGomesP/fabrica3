from sqlalchemy.orm import Session
from backend.src.components.models.medo import Medo

def create_medo(db: Session, medo_data):
    novo_medo = Medo(**medo_data)
    db.add(novo_medo)
    db.commit()  # Persiste no banco de dados
    db.refresh(novo_medo)
    return novo_medo

def get_medos(db: Session):
    return db.query(Medo).all()
