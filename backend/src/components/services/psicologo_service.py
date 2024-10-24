from sqlalchemy.orm import Session
from backend.src.components.models.psicologo import Psicologo

def create_psicologo(db: Session, psicologo_data):
    novo_psicologo = Psicologo(**psicologo_data)
    db.add(novo_psicologo)
    db.commit()  # Persiste os dados no banco de dados
    db.refresh(novo_psicologo)
    return novo_psicologo

def get_psicologos(db: Session):
    return db.query(Psicologo).all()
