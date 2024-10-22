from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.components.models.db import Base
from src.components.models.paciente import Paciente
from src.components.models.instrumento import Instrumento

class Medicao(Base):
    __tablename__ = 'tb_Medicao'

    id_medicao = Column(Integer, primary_key=True, autoincrement=True)
    nome_medicao = Column(Text, nullable=False)
    id_paciente = Column(Integer, ForeignKey('tb_Paciente.id_paciente'), nullable=False) 
    data_medicao = Column(Text, nullable=False)
    resultado_medicao = Column(String(255), nullable=False)
    id_instrumento = Column(Integer, ForeignKey('tb_Instrumento.id_instrumento'), nullable=False)

    # Relacionamentos
    paciente = relationship("Paciente", backref="medicoes")
    instrumento = relationship("Instrumento", backref="medicoes")

    def __repr__(self):
        return (f"<Medicao(id_medicao={self.id_medicao}, nome_medicao={self.nome_medicao}, "
                f"id_paciente={self.id_paciente}, data_medicao={self.data_medicao}, "
                f"resultado_medicao={self.resultado_medicao}, id_instrumento={self.id_instrumento})>")
