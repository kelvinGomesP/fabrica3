from sqlalchemy import Column, Integer, String, Date
from src.components.models.db import Base

class Paciente(Base):
    __tablename__ = 'tb_Paciente'
    id_paciente = Column(Integer, primary_key=True, autoincrement=True)  # Mudado para 'id_paciente'
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    observacao = Column(String)

    def __repr__(self):
        return f"<Paciente(id_paciente={self.id_paciente}, nome={self.nome})>"