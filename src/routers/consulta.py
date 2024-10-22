from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.components.models.consulta import Consulta
from src.components.models.db import get_db
from src.components.services.consulta_service import create_consulta, get_consultas

# Definindo o schema para as entradas (Pydantic)
class ConsultaCreate(BaseModel):
    id_paciente: int
    id_psicologo: int
    data_consulta: str
    id_vr: int = None
    id_medicao: int = None

router = APIRouter()

# Rota para criar uma nova consulta
@router.post("/consultas/")
def criar_consulta(consulta: ConsultaCreate, db: Session = Depends(get_db)):
    consulta_data = consulta.dict()
    return create_consulta(db, consulta_data)

# Rota para listar todas as consultas
@router.get("/consultas/")
def listar_consultas(db: Session = Depends(get_db)):
    return get_consultas(db)
#okay