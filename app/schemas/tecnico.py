from pydantic import BaseModel


class TecnicoCreate(BaseModel):
    nome: str
    registro: str
    telefone: str
    email: str


class TecnicoResponse(TecnicoCreate):
    id: int

    class Config:
        from_attributes = True