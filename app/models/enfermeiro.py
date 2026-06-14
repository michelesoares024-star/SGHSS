from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base


class Enfermeiro(Base):
    __tablename__ = "enfermeiros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    coren = Column(String, unique=True)
    telefone = Column(String)
    email = Column(String)