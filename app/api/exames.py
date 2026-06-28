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


@router.get(
    "/{id}",
    response_model=ExameResponse
)
def buscar_exame(
    id: int,
    db: Session = Depends(get_db)
):

    exame = db.query(
        Exame
    ).filter(
        Exame.id == id
    ).first()

    if not exame:
        raise HTTPException(
            status_code=404,
            detail="Exame não encontrado"
        )

    return exame


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

    db.add(
        novo_exame
    )

    db.commit()

    db.refresh(
        novo_exame
    )

    logger.info(
        f"Exame criado para paciente {exame.paciente_id}"
    )

    return novo_exame


@router.put(
    "/{id}",
    response_model=ExameResponse
)
def atualizar_exame(
    id: int,
    dados: ExameCreate,
    db: Session = Depends(get_db)
):

    exame = db.query(
        Exame
    ).filter(
        Exame.id == id
    ).first()

    if not exame:
        raise HTTPException(
            status_code=404,
            detail="Exame não encontrado"
        )

    paciente = db.query(
        Paciente
    ).filter(
        Paciente.id == dados.paciente_id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    exame.tipo = dados.tipo
    exame.resultado = dados.resultado
    exame.data = dados.data
    exame.paciente_id = dados.paciente_id

    db.commit()

    db.refresh(
        exame
    )

    logger.info(
        f"Exame atualizado: {id}"
    )

    return exame


@router.delete(
    "/{id}"
)
def excluir_exame(
    id: int,
    db: Session = Depends(get_db)
):

    exame = db.query(
        Exame
    ).filter(
        Exame.id == id
    ).first()

    if not exame:
        raise HTTPException(
            status_code=404,
            detail="Exame não encontrado"
        )

    db.delete(
        exame
    )

    db.commit()

    logger.info(
        f"Exame excluído: {id}"
    )

    return {
        "mensagem": "Exame excluído com sucesso"
    }