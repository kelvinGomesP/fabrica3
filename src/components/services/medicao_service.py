from sqlalchemy.orm import Session
from src.components.models.medicao import Medicao

def create_medicao(db: Session, medicao_data):
    nova_medicao = Medicao(**medicao_data)
    db.add(nova_medicao)
    db.commit()
    db.refresh(nova_medicao)
    return nova_medicao

def get_medicoes(db: Session):
    return db.query(Medicao).all()
