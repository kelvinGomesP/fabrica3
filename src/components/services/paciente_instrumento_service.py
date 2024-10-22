from sqlalchemy.orm import Session
from src.components.models.paciente_instrumento import RelPacienteInstrumento

def create_paciente_instrumento(db: Session, paciente_instrumento_data):
    nova_relacao = RelPacienteInstrumento(**paciente_instrumento_data)
    db.add(nova_relacao)
    db.commit()
    db.refresh(nova_relacao)
    return nova_relacao

def get_paciente_instrumentos(db: Session):
    return db.query(RelPacienteInstrumento).all()
