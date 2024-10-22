# src/routers/consulta.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.components.models.consulta import Consulta
from src.components.models.db import get_db
from src.components.services.consulta_service import create_consulta, get_consultas

class ConsultaCreate(BaseModel):
    id_paciente: int
    id_psicologo: int
    id_vr: int
    id_medicao: int
    data_consulta: str

router = APIRouter()

@router.post("/consultas/")
def criar_consulta(consulta: ConsultaCreate, db: Session = Depends(get_db)):
    consulta_data = consulta.dict()
    return create_consulta(db, consulta_data)

@router.get("/consultas/")
def listar_consultas(db: Session = Depends(get_db)):
    return get_consultas(db)
