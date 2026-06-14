from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger

from app.models.enfermeiro import Enfermeiro

from app.schemas.enfermeiro import (
    EnfermeiroCreate,
    EnfermeiroResponse
)

router = APIRouter(
    prefix="/enfermeiros",
    tags=["Enfermeiros"]
)


@router.get(
    "/",
    response_model=list[EnfermeiroResponse]
)
def listar_enfermeiros(
    db: Session = Depends(get_db)
):
    return db.query(
        Enfermeiro
    ).all()


@router.post(
    "/",
    response_model=EnfermeiroResponse,
    status_code=201
)
def criar_enfermeiro(
    enfermeiro: EnfermeiroCreate,
    db: Session = Depends(get_db)
):

    coren_existente = db.query(
        Enfermeiro
    ).filter(
        Enfermeiro.coren == enfermeiro.coren
    ).first()

    if coren_existente:
        raise HTTPException(
            status_code=400,
            detail="COREN já cadastrado"
        )

    novo_enfermeiro = Enfermeiro(
        nome=enfermeiro.nome,
        coren=enfermeiro.coren,
        telefone=enfermeiro.telefone,
        email=enfermeiro.email
    )

    db.add(
        novo_enfermeiro
    )

    db.commit()

    db.refresh(
        novo_enfermeiro
    )

    logger.info(
        f"Enfermeiro criado: {novo_enfermeiro.nome}"
    )

    return novo_enfermeiro