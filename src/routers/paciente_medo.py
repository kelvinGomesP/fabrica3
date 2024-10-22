from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.components.models.paciente_medo import RelPacienteMedo
from src.components.models.db import get_db
from src.components.services.paciente_medo_service import create_paciente_medo, get_paciente_medos

class PacienteMedoCreate(BaseModel):
    id_paciente: int
    id_medo: int

router = APIRouter()

@router.post("/pacientes-medos/")
def criar_paciente_medo(relacao: PacienteMedoCreate, db: Session = Depends(get_db)):
    relacao_data = relacao.dict()
    return create_paciente_medo(db, relacao_data)

@router.get("/pacientes-medos/")
def listar_paciente_medos(db: Session = Depends(get_db)):
    return get_paciente_medos(db)
