from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger

from app.models.medico import Medico
from app.models.consulta import Consulta

from app.schemas.medico import (
    MedicoCreate,
    MedicoResponse
)

router = APIRouter(
    prefix="/medicos",
    tags=["Medicos"]
)


@router.get(
    "/",
    response_model=list[MedicoResponse]
)
def listar_medicos(
    db: Session = Depends(get_db)
):
    return db.query(Medico).all()


@router.get(
    "/{id}",
    response_model=MedicoResponse
)
def buscar_medico(
    id: int,
    db: Session = Depends(get_db)
):

    medico = db.query(
        Medico
    ).filter(
        Medico.id == id
    ).first()

    if not medico:
        raise HTTPException(
            status_code=404,
            detail="Médico não encontrado"
        )

    return medico


@router.post(
    "/",
    response_model=MedicoResponse,
    status_code=201
)
def criar_medico(
    medico: MedicoCreate,
    db: Session = Depends(get_db)
):

    crm_existente = db.query(
        Medico
    ).filter(
        Medico.crm == medico.crm
    ).first()

    if crm_existente:
        raise HTTPException(
            status_code=400,
            detail="CRM já cadastrado"
        )

    novo_medico = Medico(
        nome=medico.nome,
        crm=medico.crm,
        especialidade=medico.especialidade,
        telefone=medico.telefone,
        email=medico.email
    )

    db.add(novo_medico)

    db.commit()

    db.refresh(
        novo_medico
    )
    logger.info(
        f"Médico criado: {novo_medico.nome}"
    )


    return novo_medico

@router.get(
    "/{id}/consultas"
)
def agenda_medico(
    id: int,
    db: Session = Depends(get_db)
):

    medico = db.query(
        Medico
    ).filter(
        Medico.id == id
    ).first()

    if not medico:
        raise HTTPException(
            status_code=404,
            detail="Médico não encontrado"
        )

    consultas = db.query(
        Consulta
    ).filter(
        Consulta.medico_id == id
    ).all()

    return consultas