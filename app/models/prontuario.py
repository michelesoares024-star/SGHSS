from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime


class Prontuario(Base):
    __tablename__ = "prontuarios"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))

    historico_clinico = Column(String)
    alergias = Column(String)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    paciente = relationship("Paciente", back_populates="prontuario")