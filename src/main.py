from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.components.models import Paciente, Base  # Certifique-se de que este caminho está correto

# Caminho para o banco de dados
DATABASE_URL = "sqlite:///C:/Users/e-kelvin.santos/Documents/fabrica/fabrica.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import FastAPI
from routers import paciente  # Verifique se o caminho está correto para o arquivo de rotas

app = FastAPI()

app.include_router(paciente.router)  # Incluindo as rotas do paciente
