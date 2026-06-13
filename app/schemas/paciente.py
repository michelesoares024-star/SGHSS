from datetime import date
from pydantic import BaseModel


class PacienteCreate(BaseModel):
    nome: str
    cpf: str
    telefone: str
    email: str
    endereco: str
    data_nascimento: date


class PacienteResponse(PacienteCreate):
    id: int

    class Config:
        from_attributes = True