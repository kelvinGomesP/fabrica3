from sqlalchemy import Column, Integer, String
from backend.src.components.models.db import Base

class Psicologo(Base):
    __tablename__ = 'tb_Psicologo'
    id_psicologo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    crp = Column(String, unique=True, nullable=False)  # CRP é o registro profissional do psicólogo
    telefone = Column(String)
    email = Column(String)
    especialidade = Column(String)  # Exemplo de campo adicional

    def __repr__(self):
        return f"<Psicologo(id={self.id}, nome={self.nome})>"
