from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger

from app.models.prontuario import Prontuario
from app.models.paciente import Paciente

from app.schemas.prontuario import (
    ProntuarioCreate,
    ProntuarioResponse
)


router = APIRouter(
    prefix="/prontuarios",
    tags=["Prontuarios"]
)


@router.get(
    "/",
    response_model=list[ProntuarioResponse]
)
def listar_prontuarios(
    db: Session = Depends(get_db)
):
    return db.query(
        Prontuario
    ).all()


@router.get(
    "/{id}",
    response_model=ProntuarioResponse
)
def buscar_prontuario(
    id: int,
    db: Session = Depends(get_db)
):

    prontuario = db.query(
        Prontuario
    ).filter(
        Prontuario.id == id
    ).first()

    if not prontuario:
        raise HTTPException(
            status_code=404,
            detail="Prontuário não encontrado"
        )

    return prontuario


@router.post(
    "/",
    response_model=ProntuarioResponse,
    status_code=201
)
def criar_prontuario(
    prontuario: ProntuarioCreate,
    db: Session = Depends(get_db)
):

    paciente = db.query(
        Paciente
    ).filter(
        Paciente.id == prontuario.paciente_id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    prontuario_existente = db.query(
        Prontuario
    ).filter(
        Prontuario.paciente_id == prontuario.paciente_id
    ).first()

    if prontuario_existente:
        raise HTTPException(
            status_code=400,
            detail="Paciente já possui prontuário"
        )

    novo_prontuario = Prontuario(
        paciente_id=prontuario.paciente_id,
        historico_clinico=prontuario.historico_clinico,
        alergias=prontuario.alergias
    )

    db.add(
        novo_prontuario
    )

    db.commit()

    db.refresh(
        novo_prontuario
    )

    logger.info(
        f"Prontuário criado para paciente {prontuario.paciente_id}"
    )

    return novo_prontuario


@router.put(
    "/{id}",
    response_model=ProntuarioResponse
)
def atualizar_prontuario(
    id: int,
    dados: ProntuarioCreate,
    db: Session = Depends(get_db)
):

    prontuario = db.query(
        Prontuario
    ).filter(
        Prontuario.id == id
    ).first()

    if not prontuario:
        raise HTTPException(
            status_code=404,
            detail="Prontuário não encontrado"
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

    prontuario.paciente_id = dados.paciente_id
    prontuario.historico_clinico = dados.historico_clinico
    prontuario.alergias = dados.alergias

    db.commit()

    db.refresh(
        prontuario
    )

    logger.info(
        f"Prontuário atualizado: {id}"
    )

    return prontuario


@router.delete(
    "/{id}"
)
def excluir_prontuario(
    id: int,
    db: Session = Depends(get_db)
):

    prontuario = db.query(
        Prontuario
    ).filter(
        Prontuario.id == id
    ).first()

    if not prontuario:
        raise HTTPException(
            status_code=404,
            detail="Prontuário não encontrado"
        )

    db.delete(
        prontuario
    )

    db.commit()

    logger.info(
        f"Prontuário excluído: {id}"
    )

    return {
        "mensagem": "Prontuário excluído com sucesso"
    }