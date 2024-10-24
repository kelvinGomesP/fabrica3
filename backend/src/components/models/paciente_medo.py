from sqlalchemy import Column, Integer, ForeignKey
from backend.src.components.models.db import Base

class RelPacienteMedo(Base):
    __tablename__ = 'Rel_Paciente_Medo'
    
    id_paciente = Column(Integer, ForeignKey('tb_Paciente.id_paciente'), primary_key=True)
    id_medo = Column(Integer, ForeignKey('tb_Medo.id_medo'), primary_key=True)

    def __repr__(self):
        return f"<RelPacienteMedo(id_paciente={self.id_paciente}, id_medo={self.id_medo})>"
