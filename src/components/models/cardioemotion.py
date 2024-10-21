# src/components/models/cardioemotion.py
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from src.components.models.db import Base

class CardioEmotion(Base):
    __tablename__ = 'tb_CardioEmotion'

    Id_CardioEmotion = Column(Integer, primary_key=True, index=True)
    id_instrumento = Column(Integer, ForeignKey("tb_Instrumento.id_instrumento"), nullable=False)  # Corrigido para o nome correto
    Session_datetime = Column(String, nullable=False)
    Green_percent = Column(Float)
    Blue_percent = Column(Float)
    Red_percent = Column(Float)
    Bpm_avg = Column(Integer)
    Data1 = Column(String)

    instrumento = relationship("Instrumento")  # Se você tiver um modelo Instrumento

    def __repr__(self):
        return (f"<CardioEmotion(Session_datetime={self.Session_datetime}, "
                f"Green_percent={self.Green_percent}, Blue_percent={self.Blue_percent}, "
                f"Red_percent={self.Red_percent}, Bpm_avg={self.Bpm_avg}, Data1={self.Data1})>")
