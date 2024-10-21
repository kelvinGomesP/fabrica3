from sqlalchemy import Column, Integer, String
from src.components.models.db import Base

class Medo(Base):
    __tablename__ = 'tb_Medo'
    id_medo = Column(Integer, primary_key=True, autoincrement=True)
    nome_medo = Column(String(255), nullable=False)
    grau_medo = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Medo(id_medo={self.id_medo}, nome_medo={self.nome_medo}, grau_medo={self.grau_medo})>"
