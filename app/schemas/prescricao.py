from datetime import date

from pydantic import BaseModel


class PrescricaoCreate(BaseModel):
    data: date

    medicamento: str

    orientacoes: str

    consulta_id: int


class PrescricaoResponse(
    PrescricaoCreate
):
    id: int

    class Config:
        from_attributes = True