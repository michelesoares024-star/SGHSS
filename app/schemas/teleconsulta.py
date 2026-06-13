from pydantic import BaseModel


class TeleconsultaCreate(BaseModel):
    teleconsulta: bool = True

    link: str

    consulta_id: int


class TeleconsultaResponse(
    TeleconsultaCreate
):
    id: int

    class Config:
        from_attributes = True