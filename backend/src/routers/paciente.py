from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.src.components.models.paciente import Paciente
from backend.src.components.models.db import get_db
from backend.src.components.services.paciente_service import create_paciente, get_pacientes
from backend.src.utils.helpers import format_date  # Importando a função auxiliar

class PacienteCreate(BaseModel):
    nome: str
    data_nascimento: str
    cpf: str
    telefone: str
    email: str
    endereco: str
    observacao: str = None

router = APIRouter()

@router.post("/pacientes/")
def criar_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    paciente_data = paciente.dict()
    paciente_data['data_nascimento'] = format_date(paciente_data['data_nascimento'])
    return create_paciente(db, paciente_data)

@router.get("/pacientes/")
def listar_pacientes(db: Session = Depends(get_db)):
    return get_pacientes(db)
#okay