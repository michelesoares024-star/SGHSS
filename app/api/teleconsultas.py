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


@router.get(
    "/{id}",
    response_model=TeleconsultaResponse
)
def buscar_teleconsulta(
    id: int,
    db: Session = Depends(get_db)
):

    teleconsulta = db.query(
        Teleconsulta
    ).filter(
        Teleconsulta.id == id
    ).first()

    if not teleconsulta:
        raise HTTPException(
            status_code=404,
            detail="Teleconsulta não encontrada"
        )

    return teleconsulta


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


@router.put(
    "/{id}",
    response_model=TeleconsultaResponse
)
def atualizar_teleconsulta(
    id: int,
    dados: TeleconsultaCreate,
    db: Session = Depends(get_db)
):

    teleconsulta = db.query(
        Teleconsulta
    ).filter(
        Teleconsulta.id == id
    ).first()

    if not teleconsulta:
        raise HTTPException(
            status_code=404,
            detail="Teleconsulta não encontrada"
        )

    consulta = db.query(
        Consulta
    ).filter(
        Consulta.id == dados.consulta_id
    ).first()

    if not consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada"
        )

    teleconsulta.teleconsulta = dados.teleconsulta
    teleconsulta.link = dados.link
    teleconsulta.consulta_id = dados.consulta_id

    db.commit()

    db.refresh(
        teleconsulta
    )

    logger.info(
        f"Teleconsulta atualizada: {id}"
    )

    return teleconsulta


@router.delete(
    "/{id}"
)
def excluir_teleconsulta(
    id: int,
    db: Session = Depends(get_db)
):

    teleconsulta = db.query(
        Teleconsulta
    ).filter(
        Teleconsulta.id == id
    ).first()

    if not teleconsulta:
        raise HTTPException(
            status_code=404,
            detail="Teleconsulta não encontrada"
        )

    db.delete(
        teleconsulta
    )

    db.commit()

    logger.info(
        f"Teleconsulta excluída: {id}"
    )

    return {
        "mensagem": "Teleconsulta excluída com sucesso"
    }