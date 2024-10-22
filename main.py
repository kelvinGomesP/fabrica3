from fastapi import FastAPI
from src.components.models.db import Base, engine
from src.routers.paciente import router as paciente_router
from src.routers.psicologo import router as psicologo_router
from src.routers.medo import router as medo_router
from src.routers.instrumento import router as instrumento_router
from src.routers.vr import router as vr_router
from src.routers.cardioemotion import router as cardioemotion_router
from src.routers.medicao import router as medicao_router
from src.routers.consulta import router as consulta_router
from src.routers.paciente_instrumento import router as paciente_instrumento_router
from src.routers.paciente_medo import router as paciente_medo_router

app = FastAPI()

# Incluindo rotas
app.include_router(paciente_router)
app.include_router(psicologo_router)
app.include_router(medo_router)
app.include_router(instrumento_router)
app.include_router(vr_router)
app.include_router(cardioemotion_router)
app.include_router(medicao_router)
app.include_router(consulta_router)
app.include_router(paciente_instrumento_router)
app.include_router(paciente_medo_router)


# Criando as tabelas
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API está rodando!"}
