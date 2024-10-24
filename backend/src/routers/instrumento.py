from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.src.components.models.instrumento import Instrumento
from backend.src.components.models.db import get_db
from backend.src.components.services.instrumento_service import create_instrumento, get_instrumentos

class InstrumentoCreate(BaseModel):
    nome_instrumento: str
    tipo_medicao: str

router = APIRouter()

@router.post("/instrumentos/")
def criar_instrumento(instrumento: InstrumentoCreate, db: Session = Depends(get_db)):
    instrumento_data = instrumento.dict()
    return create_instrumento(db, instrumento_data)

@router.get("/instrumentos/")
def listar_instrumentos(db: Session = Depends(get_db)):
    return get_instrumentos(db)

#OKAY