from sqlalchemy import create_engine
from src.components.models.db import Base, SQLALCHEMY_DATABASE_URL

# Cria o banco de dados e as tabelas
def init_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
