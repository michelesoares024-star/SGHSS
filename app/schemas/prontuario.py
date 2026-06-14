from datetime import datetime

from pydantic import BaseModel


class ProntuarioCreate(BaseModel):
    paciente_id: int
    historico_clinico: str
    alergias: str


class ProntuarioResponse(ProntuarioCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True