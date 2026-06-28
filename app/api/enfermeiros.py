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


@router.get(
    "/{id}",
    response_model=EnfermeiroResponse
)
def buscar_enfermeiro(
    id: int,
    db: Session = Depends(get_db)
):

    enfermeiro = db.query(
        Enfermeiro
    ).filter(
        Enfermeiro.id == id
    ).first()

    if not enfermeiro:
        raise HTTPException(
            status_code=404,
            detail="Enfermeiro não encontrado"
        )

    return enfermeiro


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


@router.put(
    "/{id}",
    response_model=EnfermeiroResponse
)
def atualizar_enfermeiro(
    id: int,
    dados: EnfermeiroCreate,
    db: Session = Depends(get_db)
):

    enfermeiro = db.query(
        Enfermeiro
    ).filter(
        Enfermeiro.id == id
    ).first()

    if not enfermeiro:
        raise HTTPException(
            status_code=404,
            detail="Enfermeiro não encontrado"
        )

    enfermeiro.nome = dados.nome
    enfermeiro.coren = dados.coren
    enfermeiro.telefone = dados.telefone
    enfermeiro.email = dados.email

    db.commit()

    db.refresh(
        enfermeiro
    )

    logger.info(
        f"Enfermeiro atualizado: {id}"
    )

    return enfermeiro


@router.delete(
    "/{id}"
)
def excluir_enfermeiro(
    id: int,
    db: Session = Depends(get_db)
):

    enfermeiro = db.query(
        Enfermeiro
    ).filter(
        Enfermeiro.id == id
    ).first()

    if not enfermeiro:
        raise HTTPException(
            status_code=404,
            detail="Enfermeiro não encontrado"
        )

    db.delete(
        enfermeiro
    )

    db.commit()

    logger.info(
        f"Enfermeiro excluído: {id}"
    )

    return {
        "mensagem": "Enfermeiro excluído com sucesso"
    }