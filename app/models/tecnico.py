from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base


class Tecnico(Base):
    __tablename__ = "tecnicos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome = Column(
        String,
        nullable=False
    )

    registro = Column(
        String,
        unique=True
    )

    telefone = Column(String)

    email = Column(String)