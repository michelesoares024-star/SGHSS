from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.core.database import Base


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    data = Column(
        Date,
        nullable=False
    )

    observacao = Column(
        String
    )

    paciente_id = Column(
        Integer,
        ForeignKey("pacientes.id")
    )

    medico_id = Column(
        Integer,
        ForeignKey("medicos.id")
    )