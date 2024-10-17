from sqlalchemy import Column, Integer, String
from src.components.db import Base

class Psicologo(Base):
    __tablename__ = "tb_Psicologo"

    Id_psicologo = Column(Integer, primary_key=True, index=True)
    Nome_psicologo = Column(String(255), nullable=False)
