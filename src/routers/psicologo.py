from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.components.models.psicologo import Psicologo
from src.components.models.db import get_db
from src.components.services.psicologo_service import create_psicologo, get_psicologos

class PsicologoCreate(BaseModel):
    nome: str
    crp: str
    telefone: str
    email: str
    especialidade: str

router = APIRouter()

@router.post("/psicologos/")
def criar_psicologo(psicologo: PsicologoCreate, db: Session = Depends(get_db)):
    psicologo_data = psicologo.dict()
    return create_psicologo(db, psicologo_data)

@router.get("/psicologos/")
def listar_psicologos(db: Session = Depends(get_db)):
    return get_psicologos(db)
