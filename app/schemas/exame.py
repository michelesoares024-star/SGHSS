from datetime import date

from pydantic import BaseModel


class ExameCreate(BaseModel):
    tipo: str
    resultado: str
    data: date
    paciente_id: int


class ExameResponse(ExameCreate):
    id: int

    class Config:
        from_attributes = True