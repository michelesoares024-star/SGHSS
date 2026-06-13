from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

from app.models.paciente import Paciente
from app.models.medico import Medico
from app.models.consulta import Consulta
from app.models.prescricao import Prescricao
from app.models.teleconsulta import Teleconsulta

from app.api.pacientes import router as pacientes_router
from app.api.medicos import router as medicos_router
from app.api.consultas import router as consultas_router
from app.api.prescricoes import router as prescricoes_router
from app.api.teleconsultas import router as teleconsultas_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SGHSS",
    version="1.0.0"
)

app.include_router(pacientes_router)
app.include_router(medicos_router)
app.include_router(consultas_router)
app.include_router(prescricoes_router)
app.include_router(teleconsultas_router)

@app.get("/")
def home():
    return {
        "sistema": "SGHSS",
        "status": "online"
    }

@app.get("/health")
def health():

    return {
        "status": "ok",
        "api": "SGHSS",
        "database": "online"
    }