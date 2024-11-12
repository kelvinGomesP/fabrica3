from sqlalchemy.orm import Session
from backend.src.components.models.paciente import Paciente
from backend.src.components.models.medo import Medo
from backend.src.components.models.paciente_medo import RelPacienteMedo

def create_paciente(db: Session, paciente_data, medo_data=None):
    # Criar o paciente
    novo_paciente = Paciente(**paciente_data)
    db.add(novo_paciente)
    db.commit()
    db.refresh(novo_paciente)

    # Criar o medo, se informado, e a relação automaticamente
    if medo_data:
        novo_medo = Medo(**medo_data)
        db.add(novo_medo)
        db.commit()
        db.refresh(novo_medo)
        
        # Criar a relação entre paciente e medo
        nova_relacao = RelPacienteMedo(id_paciente=novo_paciente.id_paciente, id_medo=novo_medo.id_medo)
        db.add(nova_relacao)
        db.commit()

    return novo_paciente

def get_pacientes(db: Session):
    return db.query(Paciente).all()
