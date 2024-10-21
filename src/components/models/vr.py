from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.components.models.db import Base

class VR(Base):
    __tablename__ = 'tb_VR'
    id_vr = Column(Integer, primary_key=True, autoincrement=True)
    data_video = Column(String, nullable=False)
    id_medo = Column(Integer, ForeignKey('tb_Medo.id_medo'), nullable=False)  # Corrija para 'tb_Medo.id_medo'

    medo = relationship("Medo")

    def __repr__(self):
        return f"<VR(id_vr={self.id_vr}, data_video={self.data_video}, id_medo={self.id_medo})>"
