# src/components/models/consulta.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.components.models.db import Base

class Consulta(Base):
    __tablename__ = 'tb_Consulta'

    id_consulta = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey('tb_Paciente.id_paciente'))  # Mudança aqui
    id_psicologo = Column(Integer, ForeignKey('tb_Psicologo.id_psicologo'))  # Mudança aqui
    id_vr = Column(Integer, ForeignKey('tb_VR.id_vr'))
    id_medicao = Column(Integer, ForeignKey('tb_Medicao.id_medicao'))
    data_consulta = Column(Date, nullable=False)

    # Relacionamentos
    paciente = relationship("Paciente", back_populates="consultas")
    psicologo = relationship("Psicologo", back_populates="consultas")
    vr = relationship("VR", back_populates="consultas")
    medicao = relationship("Medicao", back_populates="consultas")

    def __repr__(self):
        return f"<Consulta(id_consulta={self.id_consulta}, id_paciente={self.id_paciente}, data_consulta={self.data_consulta})>"
