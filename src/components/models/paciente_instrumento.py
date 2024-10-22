from sqlalchemy import Column, Integer, ForeignKey
from src.components.models.db import Base

class RelPacienteInstrumento(Base):
    __tablename__ = 'Rel_Paciente_Instrumento'
    
    id_paciente = Column(Integer, ForeignKey('tb_Paciente.id_paciente'), primary_key=True)
    id_instrumento = Column(Integer, ForeignKey('tb_Instrumento.id_instrumento'), primary_key=True)

    def __repr__(self):
        return f"<RelPacienteInstrumento(id_paciente={self.id_paciente}, id_instrumento={self.id_instrumento})>"
