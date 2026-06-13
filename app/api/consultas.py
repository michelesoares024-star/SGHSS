from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.core.logger import logger

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.consulta import Consulta
from app.models.paciente import Paciente
from app.models.medico import Medico

from app.schemas.consulta import (
    ConsultaCreate,
    ConsultaResponse
)

router = APIRouter(
    prefix="/consultas",
    tags=["Consultas"]
)


@router.get(
    "/",
    response_model=list[ConsultaResponse]
)
def listar_consultas(
    db: Session = Depends(get_db)
):
    return db.query(
        Consulta
    ).all()


@router.post(
    "/",
    response_model=ConsultaResponse,
    status_code=201
)
def criar_consulta(
    consulta: ConsultaCreate,
    db: Session = Depends(get_db)
):

    paciente = db.query(
        Paciente
    ).filter(
        Paciente.id == consulta.paciente_id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    medico = db.query(
        Medico
    ).filter(
        Medico.id == consulta.medico_id
    ).first()

    if not medico:
        raise HTTPException(
            status_code=404,
            detail="Médico não encontrado"
        )

    nova_consulta = Consulta(
        data=consulta.data,
        observacao=consulta.observacao,
        paciente_id=consulta.paciente_id,
        medico_id=consulta.medico_id
    )

    db.add(
        nova_consulta
    )

    db.commit()

    db.refresh(
        nova_consulta
    )

    logger.info(
    f"Consulta criada | Paciente {consulta.paciente_id} | Médico {consulta.medico_id}"
    )

    return nova_consulta


@router.put(
    "/{id}",
    response_model=ConsultaResponse
)
def atualizar_consulta(
    id: int,
    dados: ConsultaCreate,
    db: Session = Depends(get_db)
):

    consulta = db.query(
        Consulta
    ).filter(
        Consulta.id == id
    ).first()

    if not consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada"
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

    medico = db.query(
        Medico
    ).filter(
        Medico.id == dados.medico_id
    ).first()

    if not medico:
        raise HTTPException(
            status_code=404,
            detail="Médico não encontrado"
        )

    consulta.data = dados.data
    consulta.observacao = dados.observacao
    consulta.paciente_id = dados.paciente_id
    consulta.medico_id = dados.medico_id

    db.commit()

    db.refresh(
        consulta
    )

    return consulta


@router.delete(
    "/{id}"
)
def excluir_consulta(
    id: int,
    db: Session = Depends(get_db)
):

    consulta = db.query(
        Consulta
    ).filter(
        Consulta.id == id
    ).first()

    if not consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada"
        )

    db.delete(
        consulta
    )

    db.commit()

    logger.info(
    f"Consulta removida {id}"
    )

    return {
        "mensagem": "Consulta excluída com sucesso"
    }