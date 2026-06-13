from datetime import date

from pydantic import BaseModel


class ConsultaCreate(BaseModel):
    data: date
    observacao: str

    paciente_id: int
    medico_id: int


class ConsultaResponse(ConsultaCreate):
    id: int

    class Config:
        from_attributes = True