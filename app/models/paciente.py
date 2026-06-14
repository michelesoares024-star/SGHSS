from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.orm import relationship

from app.core.database import Base


class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    data_nascimento = Column(Date)
    prontuario = relationship("Prontuario", uselist=False, back_populates="paciente")