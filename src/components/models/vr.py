from sqlalchemy import Column, Integer, String, ForeignKey
from src.components.db import Base

class VR(Base):
    __tablename__ = "tb_VR"

    Id_vr = Column(Integer, primary_key=True, index=True)
    Data_video = Column(String, nullable=False)
    Id_medo = Column(Integer, ForeignKey("tb_Medo.Id_medo"))
