from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.core.database import Base


class Teleconsulta(Base):
    __tablename__ = "teleconsultas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    teleconsulta = Column(
        Boolean,
        default=True
    )

    link = Column(
        String
    )

    consulta_id = Column(
        Integer,
        ForeignKey(
            "consultas.id"
        )
    )