from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.components.models.db import Base
from src.components.models.instrumento import Instrumento 

class CardioEmotion(Base):
    __tablename__ = 'tb_CardioEmotion'

    id_cardioemotion = Column(Integer, primary_key=True, autoincrement=True)
    id_instrumento = Column(Integer, ForeignKey('tb_Instrumento.id_instrumento'), nullable=False)
    session_datetime = Column(Text, nullable=False)
    green_percent = Column(Float)
    blue_percent = Column(Float)
    red_percent = Column(Float)
    bpm_avg = Column(Integer)
    data1 = Column(String(255))

    # Definindo o relacionamento com o Instrumento
    instrumento = relationship("Instrumento", backref="cardio_emotions")

    def __repr__(self):
        return (f"<CardioEmotion(id_cardioemotion={self.id_cardioemotion}, "
                f"id_instrumento={self.id_instrumento}, session_datetime={self.session_datetime}, "
                f"green_percent={self.green_percent}, blue_percent={self.blue_percent}, "
                f"red_percent={self.red_percent}, bpm_avg={self.bpm_avg}, data1={self.data1})>")
