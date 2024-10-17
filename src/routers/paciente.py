from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.components.models import paciente
from src.main import get_db

router = APIRouter()

# Criar um novo paciente
@router.post("/pacientes/")
def create_paciente(paciente: Paciente, db: Session = Depends(get_db)):
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente

# Listar todos os pacientes
@router.get("/pacientes/")
def read_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pacientes = db.query(Paciente).offset(skip).limit(limit).all()
    return pacientes
