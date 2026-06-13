from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger

from app.models.prescricao import Prescricao
from app.models.consulta import Consulta

from app.schemas.prescricao import (
    PrescricaoCreate,
    PrescricaoResponse
)

router = APIRouter(
    prefix="/prescricoes",
    tags=["Prescricoes"]
)


@router.get(
    "/",
    response_model=list[PrescricaoResponse]
)
def listar_prescricoes(
    db: Session = Depends(get_db)
):

    return db.query(
        Prescricao
    ).all()


@router.post(
    "/",
    response_model=PrescricaoResponse,
    status_code=201
)
def criar_prescricao(
    prescricao: PrescricaoCreate,
    db: Session = Depends(get_db)
):

    consulta = db.query(
        Consulta
    ).filter(
        Consulta.id == prescricao.consulta_id
    ).first()

    if not consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada"
        )

    nova_prescricao = Prescricao(
        data=prescricao.data,
        medicamento=prescricao.medicamento,
        orientacoes=prescricao.orientacoes,
        consulta_id=prescricao.consulta_id
    )

    db.add(
        nova_prescricao
    )

    db.commit()

    db.refresh(
        nova_prescricao
    )

    logger.info(
        f"Prescrição criada para consulta {prescricao.consulta_id}"
    )

    return nova_prescricao