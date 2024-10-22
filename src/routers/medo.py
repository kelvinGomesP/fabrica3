from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.components.models.medo import Medo
from src.components.models.db import get_db
from src.components.services.medo_service import create_medo, get_medos

class MedoCreate(BaseModel):
    nome_medo: str
    grau_medo: int

router = APIRouter()

@router.post("/medos/")
def criar_medo(medo: MedoCreate, db: Session = Depends(get_db)):
    medo_data = medo.dict()
    return create_medo(db, medo_data)

@router.get("/medos/")
def listar_medos(db: Session = Depends(get_db)):
    return get_medos(db)
#OKAY