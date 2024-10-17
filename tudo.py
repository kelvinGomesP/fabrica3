
'''
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

DATABASE_URL = "sqlite:///./db.sqlite"

# Configuração do banco de dados
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelos

class Paciente(Base):
    __tablename__ = 'tb_Paciente'
    Id_paciente = Column(Integer, primary_key=True, index=True)
    Nome_paciente = Column(String, nullable=False)
    Data_nascimento = Column(Date, nullable=False)
    Sexo = Column(String, nullable=False)
    Observacao_saude = Column(String)

class Psicologo(Base):
    __tablename__ = 'tb_Psicologo'
    Id_psicologo = Column(Integer, primary_key=True, index=True)
    Nome_psicologo = Column(String, nullable=False)

class Instrumento(Base):
    __tablename__ = 'tb_Instrumento'
    Id_instrumento = Column(Integer, primary_key=True, index=True)
    Nome_instrumento = Column(String, nullable=False)
    Tipo_medicao = Column(String, nullable=False)

class VR(Base):
    __tablename__ = 'tb_VR'
    Id_vr = Column(Integer, primary_key=True, index=True)
    Data_video = Column(String, nullable=False)
    Id_medo = Column(Integer, ForeignKey("tb_Medo.Id_medo"))

class Medo(Base):
    __tablename__ = 'tb_Medo'
    Id_medo = Column(Integer, primary_key=True, index=True)
    Nome_medo = Column(String, nullable=False)
    Grau_medo = Column(Integer, nullable=False)

class Medicao(Base):
    __tablename__ = 'tb_Medicao'
    Id_medicao = Column(Integer, primary_key=True, index=True)
    Nome_medicao = Column(String, nullable=False)
    Id_paciente = Column(Integer, ForeignKey("tb_Paciente.Id_paciente"), nullable=False)
    Data_medicao = Column(String, nullable=False)
    Resultado_medicao = Column(String, nullable=False)
    Id_instrumento = Column(Integer, ForeignKey("tb_Instrumento.Id_instrumento"), nullable=False)

class Consulta(Base):
    __tablename__ = 'tb_Consulta'
    Id_consulta = Column(Integer, primary_key=True, index=True)
    Id_paciente = Column(Integer, ForeignKey("tb_Paciente.Id_paciente"), nullable=False)
    Id_psicologo = Column(Integer, ForeignKey("tb_Psicologo.Id_psicologo"), nullable=False)
    Data_consulta = Column(String, nullable=False)

# Inicializar o banco de dados
Base.metadata.create_all(bind=engine)

# CRUD completo

# 1. Paciente - CRUD
@app.post("/pacientes/")
def create_paciente(paciente: Paciente, db: Session = Depends(get_db)):
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente

@app.get("/pacientes/")
def read_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Paciente).offset(skip).limit(limit).all()

@app.get("/pacientes/{paciente_id}")
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.Id_paciente == paciente_id).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente

@app.put("/pacientes/{paciente_id}")
def update_paciente(paciente_id: int, updated_paciente: Paciente, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.Id_paciente == paciente_id).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    paciente.Nome_paciente = updated_paciente.Nome_paciente
    paciente.Data_nascimento = updated_paciente.Data_nascimento
    paciente.Sexo = updated_paciente.Sexo
    paciente.Observacao_saude = updated_paciente.Observacao_saude
    db.commit()
    db.refresh(paciente)
    return paciente

@app.delete("/pacientes/{paciente_id}")
def delete_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.Id_paciente == paciente_id).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    db.delete(paciente)
    db.commit()
    return {"detail": "Paciente deletado com sucesso"}

# 2. Psicologo - CRUD
@app.post("/psicologos/")
def create_psicologo(psicologo: Psicologo, db: Session = Depends(get_db)):
    db.add(psicologo)
    db.commit()
    db.refresh(psicologo)
    return psicologo

@app.get("/psicologos/")
def read_psicologos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Psicologo).offset(skip).limit(limit).all()

@app.get("/psicologos/{psicologo_id}")
def read_psicologo(psicologo_id: int, db: Session = Depends(get_db)):
    psicologo = db.query(Psicologo).filter(Psicologo.Id_psicologo == psicologo_id).first()
    if psicologo is None:
        raise HTTPException(status_code=404, detail="Psicologo não encontrado")
    return psicologo

@app.put("/psicologos/{psicologo_id}")
def update_psicologo(psicologo_id: int, updated_psicologo: Psicologo, db: Session = Depends(get_db)):
    psicologo = db.query(Psicologo).filter(Psicologo.Id_psicologo == psicologo_id).first()
    if psicologo is None:
        raise HTTPException(status_code=404, detail="Psicologo não encontrado")
    psicologo.Nome_psicologo = updated_psicologo.Nome_psicologo
    db.commit()
    db.refresh(psicologo)
    return psicologo

@app.delete("/psicologos/{psicologo_id}")
def delete_psicologo(psicologo_id: int, db: Session = Depends(get_db)):
    psicologo = db.query(Psicologo).filter(Psicologo.Id_psicologo == psicologo_id).first()
    if psicologo is None:
        raise HTTPException(status_code=404, detail="Psicologo não encontrado")
    db.delete(psicologo)
    db.commit()
    return {"detail": "Psicologo deletado com sucesso"}

# 3. Instrumento - CRUD
@app.post("/instrumentos/")
def create_instrumento(instrumento: Instrumento, db: Session = Depends(get_db)):
    db.add(instrumento)
    db.commit()
    db.refresh(instrumento)
    return instrumento

@app.get("/instrumentos/")
def read_instrumentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Instrumento).offset(skip).limit(limit).all()

@app.get("/instrumentos/{instrumento_id}")
def read_instrumento(instrumento_id: int, db: Session = Depends(get_db)):
    instrumento = db.query(Instrumento).filter(Instrumento.Id_instrumento == instrumento_id).first()
    if instrumento is None:
        raise HTTPException(status_code=404, detail="Instrumento não encontrado")
    return instrumento

@app.put("/instrumentos/{instrumento_id}")
def update_instrumento(instrumento_id: int, updated_instrumento: Instrumento, db: Session = Depends(get_db)):
    instrumento = db.query(Instrumento).filter(Instrumento.Id_instrumento == instrumento_id).first()
    if instrumento is None:
        raise HTTPException(status_code=404, detail="Instrumento não encontrado")
    instrumento.Nome_instrumento = updated_instrumento.Nome_instrumento
    instrumento.Tipo_medicao = updated_instrumento.Tipo_medicao
    db.commit()
    db.refresh(instrumento)
    return instrumento

@app.delete("/instrumentos/{instrumento_id}")
def delete_instrumento(instrumento_id: int, db: Session = Depends(get_db)):
    instrumento = db.query(Instrumento).filter(Instrumento.Id_instrumento == instrumento_id).first()
    if instrumento is None:
        raise HTTPException(status_code=404, detail="Instrumento não encontrado")
    db.delete(instrumento)
    db.commit()
    return {"detail": "Instrumento deletado com sucesso"}

# 4. VR - CRUD
@app.post("/vr/")
def create_vr(vr: VR, db: Session = Depends(get_db)):
    db.add(vr)
    db.commit()
    db.refresh(vr)
    return vr

@app.get("/vr/")
def read_vr(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(VR).offset(skip).limit(limit).all()

@app.get("/vr/{vr_id}")
def read_vr(vr_id: int, db: Session = Depends(get_db)):
    vr = db.query(VR).filter(VR.Id_vr == vr_id).first()
    if vr is None:
        raise HTTPException(status_code=404, detail="VR não encontrado")
    return vr

@app.put("/vr/{vr_id}")
def update_vr(vr_id: int, updated_vr: VR, db: Session = Depends(get_db)):
    vr = db.query(VR).filter(VR.Id_vr == vr_id).first()
    if vr is None:
        raise HTTPException(status_code=404, detail="VR não encontrado")
    vr.Data_video = updated_vr.Data_video
    vr.Id_medo = updated_vr.Id_medo
    db.commit()
    db.refresh(vr)
    return vr

@app.delete("/vr/{vr_id}")
def delete_vr(vr_id: int, db: Session = Depends(get_db)):
    vr = db.query(VR).filter(VR.Id_vr == vr_id).first()
    if vr is None:
        raise HTTPException(status_code=404, detail="VR não encontrado")
    db.delete(vr)
    db.commit()
    return {"detail": "VR deletado com sucesso"}

# 5. Medo - CRUD
@app.post("/medos/")
def create_medo(medo: Medo, db: Session = Depends(get_db)):
    db.add(medo)
    db.commit()
    db.refresh(medo)
    return medo

@app.get("/medos/")
def read_medos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Medo).offset(skip).limit(limit).all()

@app.get("/medos/{medo_id}")
def read_medo(medo_id: int, db: Session = Depends(get_db)):
    medo = db.query(Medo).filter(Medo.Id_medo == medo_id).first()
    if medo is None:
        raise HTTPException(status_code=404, detail="Medo não encontrado")
    return medo

@app.put("/medos/{medo_id}")
def update_medo(medo_id: int, updated_medo: Medo, db: Session = Depends(get_db)):
    medo = db.query(Medo).filter(Medo.Id_medo == medo_id).first()
    if medo is None:
        raise HTTPException(status_code=404, detail="Medo não encontrado")
    medo.Nome_medo = updated_medo.Nome_medo
    medo.Grau_medo = updated_medo.Grau_medo
    db.commit()
    db.refresh(medo)
    return medo

@app.delete("/medos/{medo_id}")
def delete_medo(medo_id: int, db: Session = Depends(get_db)):
    medo = db.query(Medo).filter(Medo.Id_medo == medo_id).first()
    if medo is None:
        raise HTTPException(status_code=404, detail="Medo não encontrado")
    db.delete(medo)
    db.commit()
    return {"detail": "Medo deletado com sucesso"}

# 6. Medicao - CRUD
@app.post("/medicoes/")
def create_medicao(medicao: Medicao, db: Session = Depends(get_db)):
    db.add(medicao)
    db.commit()
    db.refresh(medicao)
    return medicao

@app.get("/medicoes/")
def read_medicoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Medicao).offset(skip).limit(limit).all()

@app.get("/medicoes/{medicao_id}")
def read_medicao(medicao_id: int, db: Session = Depends(get_db)):
    medicao = db.query(Medicao).filter(Medicao.Id_medicao == medicao_id).first()
    if medicao is None:
        raise HTTPException(status_code=404, detail="Medicao não encontrada")
    return medicao

@app.put("/medicoes/{medicao_id}")
def update_medicao(medicao_id: int, updated_medicao: Medicao, db: Session = Depends(get_db)):
    medicao = db.query(Medicao).filter(Medicao.Id_medicao == medicao_id).first()
    if medicao is None:
        raise HTTPException(status_code=404, detail="Medicao não encontrada")
    medicao.Nome_medicao = updated_medicao.Nome_medicao
    medicao.Id_paciente = updated_medicao.Id_paciente
    medicao.Data_medicao = updated_medicao.Data_medicao
    medicao.Resultado_medicao = updated_medicao.Resultado_medicao
    medicao.Id_instrumento = updated_medicao.Id_instrumento
    db.commit()
    db.refresh(medicao)
    return medicao

@app.delete("/medicoes/{medicao_id}")
def delete_medicao(medicao_id: int, db: Session = Depends(get_db)):
    medicao = db.query(Medicao).filter(Medicao.Id_medicao == medicao_id).first()
    if medicao is None:
        raise HTTPException(status_code=404, detail="Medicao não encontrada")
    db.delete(medicao)
    db.commit()
    return {"detail": "Medicao deletada com sucesso"}

# 7. Consulta - Atualizar data da consulta
@app.put("/consultas/{consulta_id}")
def update_consulta_data(consulta_id: int, data_consulta: str, db: Session = Depends(get_db)):
    consulta = db.query(Consulta).filter(Consulta.Id_consulta == consulta_id).first()
    if consulta is None:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    consulta.Data_consulta = data_consulta
    db.commit()
    db.refresh(consulta)
    return consulta
'''