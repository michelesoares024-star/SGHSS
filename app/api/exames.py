from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger

from app.models.exame import Exame
from app.models.paciente import Paciente

from app.schemas.exame import (
    ExameCreate,
    ExameResponse
)


router = APIRouter(
    prefix="/exames",
    tags=["Exames"]
)


@router.get(
    "/",
    response_model=list[ExameResponse]
)
def listar_exames(
    db: Session = Depends(get_db)
):
    return db.query(
        Exame
    ).all()


@router.post(
    "/",
    response_model=ExameResponse,
    status_code=201
)
def criar_exame(
    exame: ExameCreate,
    db: Session = Depends(get_db)
):

    paciente = db.query(
        Paciente
    ).filter(
        Paciente.id == exame.paciente_id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    novo_exame = Exame(
        tipo=exame.tipo,
        resultado=exame.resultado,
        data=exame.data,
        paciente_id=exame.paciente_id
    )

    db.add(novo_exame)
    db.commit()
    db.refresh(novo_exame)

    logger.info(
        f"Exame criado para paciente {exame.paciente_id}"
    )

    return novo_exame