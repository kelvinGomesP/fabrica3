from sqlalchemy.orm import Session
from backend.src.components.models.paciente import Paciente

def create_paciente(db: Session, paciente_data):
    novo_paciente = Paciente(**paciente_data)
    db.add(novo_paciente)
    db.commit()
    db.refresh(novo_paciente)
    return novo_paciente

def get_pacientes(db: Session):
    return db.query(Paciente).all()