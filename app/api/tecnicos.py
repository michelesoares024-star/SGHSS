from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger

from app.models.tecnico import Tecnico

from app.schemas.tecnico import (
    TecnicoCreate,
    TecnicoResponse
)

router = APIRouter(
    prefix="/tecnicos",
    tags=["Tecnicos"]
)


@router.get(
    "/",
    response_model=list[TecnicoResponse]
)
def listar_tecnicos(
    db: Session = Depends(get_db)
):
    return db.query(
        Tecnico
    ).all()


@router.post(
    "/",
    response_model=TecnicoResponse,
    status_code=201
)
def criar_tecnico(
    tecnico: TecnicoCreate,
    db: Session = Depends(get_db)
):

    registro_existente = db.query(
        Tecnico
    ).filter(
        Tecnico.registro == tecnico.registro
    ).first()

    if registro_existente:
        raise HTTPException(
            status_code=400,
            detail="Registro já cadastrado"
        )

    novo_tecnico = Tecnico(
        nome=tecnico.nome,
        registro=tecnico.registro,
        telefone=tecnico.telefone,
        email=tecnico.email
    )

    db.add(novo_tecnico)

    db.commit()

    db.refresh(novo_tecnico)

    logger.info(
        f"Técnico criado: {novo_tecnico.nome}"
    )

    return novo_tecnico