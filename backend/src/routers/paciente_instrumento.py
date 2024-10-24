from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.src.components.models.paciente_instrumento import RelPacienteInstrumento
from backend.src.components.models.db import get_db
from backend.src.components.services.paciente_instrumento_service import create_paciente_instrumento, get_paciente_instrumentos

class PacienteInstrumentoCreate(BaseModel):
    id_paciente: int
    id_instrumento: int

router = APIRouter()

@router.post("/pacientes-instrumentos/")
def criar_paciente_instrumento(relacao: PacienteInstrumentoCreate, db: Session = Depends(get_db)):
    relacao_data = relacao.dict()
    return create_paciente_instrumento(db, relacao_data)

@router.get("/pacientes-instrumentos/")
def listar_paciente_instrumentos(db: Session = Depends(get_db)):
    return get_paciente_instrumentos(db)
