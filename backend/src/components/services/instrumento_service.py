from sqlalchemy.orm import Session
from backend.src.components.models.instrumento import Instrumento

def create_instrumento(db: Session, instrumento_data):
    novo_instrumento = Instrumento(**instrumento_data)
    db.add(novo_instrumento)
    db.commit()  # Persiste no banco de dados
    db.refresh(novo_instrumento)
    return novo_instrumento

def get_instrumentos(db: Session):
    return db.query(Instrumento).all()
