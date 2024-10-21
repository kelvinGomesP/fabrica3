from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.components.models.vr import VR
from src.components.models.db import get_db
from src.components.services.vr_service import create_vr, get_vr

class VRCreate(BaseModel):
    data_video: str
    id_medo: int

router = APIRouter()

@router.post("/vr/")
def criar_vr(vr: VRCreate, db: Session = Depends(get_db)):
    vr_data = vr.dict()
    return create_vr(db, vr_data)

@router.get("/vr/")
def listar_vr(db: Session = Depends(get_db)):
    return get_vr(db)
