from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import ForeignKey

from app.core.database import Base


class Exame(Base):
    __tablename__ = "exames"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    tipo = Column(
        String,
        nullable=False
    )

    resultado = Column(
        String
    )

    data = Column(
        Date
    )

    paciente_id = Column(
        Integer,
        ForeignKey(
            "pacientes.id"
        )
    )