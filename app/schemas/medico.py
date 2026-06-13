from pydantic import BaseModel


class MedicoCreate(BaseModel):
    nome: str
    crm: str
    especialidade: str
    telefone: str
    email: str


class MedicoResponse(MedicoCreate):
    id: int

    class Config:
        from_attributes = True