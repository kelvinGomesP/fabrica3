from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.src.components.models.db import get_db
from backend.src.components.services.medicao_service import create_medicao, get_medicoes

# Definir o esquema Pydantic para validação de entrada
class MedicaoCreate(BaseModel):
    nome_medicao: str
    id_paciente: int
    data_medicao: str
    resultado_medicao: str
    id_instrumento: int

router = APIRouter()

# Rota para criar uma nova medição
@router.post("/medicoes/")
def criar_medicao(medicao: MedicaoCreate, db: Session = Depends(get_db)):
    medicao_data = medicao.dict()
    return create_medicao(db, medicao_data)

# Rota para listar todas as medições
@router.get("/medicoes/")
def listar_medicoes(db: Session = Depends(get_db)):
    return get_medicoes(db)

#OKAY