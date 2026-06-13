from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger

from app.models.teleconsulta import Teleconsulta
from app.models.consulta import Consulta

from app.schemas.teleconsulta import (
    TeleconsultaCreate,
    TeleconsultaResponse
)

router = APIRouter(
    prefix="/teleconsultas",
    tags=["Teleconsultas"]
)


@router.get(
    "/",
    response_model=list[TeleconsultaResponse]
)
def listar_teleconsultas(
    db: Session = Depends(get_db)
):

    return db.query(
        Teleconsulta
    ).all()


@router.post(
    "/",
    response_model=TeleconsultaResponse,
    status_code=201
)
def criar_teleconsulta(
    teleconsulta: TeleconsultaCreate,
    db: Session = Depends(get_db)
):

    consulta = db.query(
        Consulta
    ).filter(
        Consulta.id == teleconsulta.consulta_id
    ).first()

    if not consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada"
        )

    nova_teleconsulta = Teleconsulta(
        teleconsulta=teleconsulta.teleconsulta,
        link=teleconsulta.link,
        consulta_id=teleconsulta.consulta_id
    )

    db.add(
        nova_teleconsulta
    )

    db.commit()

    db.refresh(
        nova_teleconsulta
    )

    logger.info(
        f"Teleconsulta criada para consulta {teleconsulta.consulta_id}"
    )

    return nova_teleconsulta