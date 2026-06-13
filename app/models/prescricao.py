from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import ForeignKey

from app.core.database import Base


class Prescricao(Base):
    __tablename__ = "prescricoes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    data = Column(
        Date
    )

    medicamento = Column(
        String,
        nullable=False
    )

    orientacoes = Column(
        String
    )

    consulta_id = Column(
        Integer,
        ForeignKey(
            "consultas.id"
        )
    )