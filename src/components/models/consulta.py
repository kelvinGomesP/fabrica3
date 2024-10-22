from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from src.components.models.db import Base

class Consulta(Base):
    __tablename__ = 'tb_Consulta'
    
    id_consulta = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey('tb_Paciente.id_paciente'), nullable=False)
    id_psicologo = Column(Integer, ForeignKey('tb_Psicologo.id_psicologo'), nullable=False)
    data_consulta = Column(String, nullable=False)
    id_vr = Column(Integer, ForeignKey('tb_VR.id_vr'))
    id_medicao = Column(Integer, ForeignKey('tb_Medicao.id_medicao'))
    
    # Relacionamentos (se necessário)
    paciente = relationship("Paciente")
    psicologo = relationship("Psicologo")
    vr = relationship("VR")
    medicao = relationship("Medicao")

    def __repr__(self):
        return f"<Consulta(id_consulta={self.id_consulta}, data_consulta={self.data_consulta})>"
