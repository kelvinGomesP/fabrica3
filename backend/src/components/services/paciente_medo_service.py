from sqlalchemy.orm import Session
from backend.src.components.models.paciente_medo import RelPacienteMedo

def create_paciente_medo(db: Session, paciente_medo_data):
    nova_relacao = RelPacienteMedo(**paciente_medo_data)
    db.add(nova_relacao)
    db.commit()
    db.refresh(nova_relacao)
    return nova_relacao

def get_paciente_medos(db: Session):
    return db.query(RelPacienteMedo).all()
