from sqlalchemy import Column, Integer, String
from src.components.db import Base

class Instrumento(Base):
    __tablename__ = "tb_Instrumento"

    Id_instrumento = Column(Integer, primary_key=True, index=True)
    Nome_instrumento = Column(String, nullable=False)
    Tipo_medicao = Column(String, nullable=False)
