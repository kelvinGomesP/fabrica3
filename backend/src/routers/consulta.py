from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.src.components.models.consulta import Consulta
from backend.src.components.models.db import get_db
from backend.src.components.services.consulta_service import create_consulta, get_consultas
from typing import Optional

class ConsultaCreate(BaseModel):
    id_paciente: int  # ID do paciente (obrigatório)
    id_psicologo: int  # ID do psicólogo (obrigatório)
    data_consulta: str  # Data da consulta (obrigatório)
    id_vr: Optional[int] = None  # ID do VR (opcional)
    id_medicao: Optional[int] = None  # ID da Medição (opcional)

router = APIRouter()

@router.post("/consultas/")
def criar_consulta_endpoint(consulta_data: ConsultaCreate, db: Session = Depends(get_db)):
    return create_consulta(db, consulta_data.dict())

@router.get("/consultas/")
async def listar_consultas(db: Session = Depends(get_db)):  # Corrigido para passar o db como dependência
    consultas = db.query(Consulta).all()  # Exemplo de consulta ao banco de dados
    return consultas