# src/components/services/consulta_service.py
from sqlalchemy.orm import Session
from src.components.models.consulta import Consulta

def create_consulta(db: Session, consulta_data):
    nova_consulta = Consulta(**consulta_data)
    db.add(nova_consulta)
    db.commit()
    db.refresh(nova_consulta)
    return nova_consulta

def get_consultas(db: Session):
    return db.query(Consulta).all()
