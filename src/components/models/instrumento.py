# src/components/models/instrumento.py
from sqlalchemy import Column, Integer, String
from src.components.models.db import Base

class Instrumento(Base):
    __tablename__ = 'tb_Instrumento'
    
    id_instrumento = Column(Integer, primary_key=True, autoincrement=True)
    nome_instrumento = Column(String, nullable=False)
    tipo_medicao = Column(String, nullable=False)

    def __repr__(self):
        return (f"<Instrumento(id_instrumento={self.id_instrumento}, "
                f"nome_instrumento={self.nome_instrumento}, tipo_medicao={self.tipo_medicao})>")
