from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.src.components.services.paciente_service import create_paciente, get_pacientes
from backend.src.components.models.db import get_db
from backend.src.utils.helpers import format_date
from backend.src.components.models.paciente import Paciente
from backend.src.components.models.psicologo import Psicologo

# Atualizar o esquema do medo para receber o medo opcionalmente
class MedoCreate(BaseModel):
    nome_medo: str
    grau_medo: int

class PacienteCreate(BaseModel):
    nome: str
    data_nascimento: str
    cpf: str
    telefone: str
    email: str
    endereco: str
    observacao: str = None
    medo: MedoCreate = None  # Medo opcional

router = APIRouter()


@router.post("/pacientes/")
def criar_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    paciente_data = paciente.dict()
    paciente_data['data_nascimento'] = format_date(paciente_data['data_nascimento'])
    
    # Extrair dados do medo
    medo_data = paciente_data.pop("medo", None)  # Remove e armazena dados de medo (se existirem)

    # Enviar para o serviço
    return create_paciente(db, paciente_data, medo_data)


@router.get("/pacientes/")
def listar_pacientes(db: Session = Depends(get_db)):
    pacientes = db.query(Paciente).all()
    return pacientes

@router.get("/psicologos/")
def listar_psicologos(db: Session = Depends(get_db)):
    psicologos = db.query(Psicologo).all()
    return psicologos

@router.get("/pacientes/")
def listar_pacientes(db: Session = Depends(get_db)):
    return get_pacientes(db)




