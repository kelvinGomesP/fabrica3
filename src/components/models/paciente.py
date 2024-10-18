from sqlalchemy import Column, Integer, String, Date
from src.components.models.db import Base

class Paciente(Base):
    __tablename__ = 'tb_Paciente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)

    def __repr__(self):
        return f"<Paciente(id={self.id}, nome={self.nome})>"
