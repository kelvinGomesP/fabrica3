from fastapi import FastAPI
from src.routers.paciente import router as paciente_router  # Importa o router dos pacientes
from src.components.models.db import Base, engine           # Conexão com o banco de dados

# Cria a aplicação FastAPI
app = FastAPI()

# Inclui as rotas do paciente
app.include_router(paciente_router)

# Inicializa o banco de dados (cria as tabelas)
Base.metadata.create_all(bind=engine)

# Rota principal para verificar se a API está funcionando
@app.get("/")
def read_root():
    return {"message": "API de Pacientes está rodando. Acesse /pacientes para interagir."}
