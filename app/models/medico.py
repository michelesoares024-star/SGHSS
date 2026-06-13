from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base


class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(
        String,
        nullable=False
    )

    crm = Column(
        String,
        unique=True
    )

    especialidade = Column(String)

    telefone = Column(String)

    email = Column(String)