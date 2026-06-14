from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.prontuario import Prontuario
from app.schemas.prontuario import ProntuarioCreate

router = APIRouter(prefix="/prontuarios", tags=["Prontuarios"])


@router.post("/")
def criar_prontuario(prontuario: ProntuarioCreate, db: Session = Depends(get_db)):
    novo = Prontuario(**prontuario.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo