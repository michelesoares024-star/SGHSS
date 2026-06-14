from pydantic import BaseModel


class EnfermeiroCreate(BaseModel):
    nome: str
    coren: str
    telefone: str
    email: str


class EnfermeiroResponse(EnfermeiroCreate):
    id: int

    class Config:
        from_attributes = True