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


@router.get(
    "/{id}",
    response_model=TecnicoResponse
)
def buscar_tecnico(
    id: int,
    db: Session = Depends(get_db)
):

    tecnico = db.query(
        Tecnico
    ).filter(
        Tecnico.id == id
    ).first()

    if not tecnico:
        raise HTTPException(
            status_code=404,
            detail="Técnico não encontrado"
        )

    return tecnico


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

    db.add(
        novo_tecnico
    )

    db.commit()

    db.refresh(
        novo_tecnico
    )

    logger.info(
        f"Técnico criado: {novo_tecnico.nome}"
    )

    return novo_tecnico


@router.put(
    "/{id}",
    response_model=TecnicoResponse
)
def atualizar_tecnico(
    id: int,
    dados: TecnicoCreate,
    db: Session = Depends(get_db)
):

    tecnico = db.query(
        Tecnico
    ).filter(
        Tecnico.id == id
    ).first()

    if not tecnico:
        raise HTTPException(
            status_code=404,
            detail="Técnico não encontrado"
        )

    tecnico.nome = dados.nome
    tecnico.registro = dados.registro
    tecnico.telefone = dados.telefone
    tecnico.email = dados.email

    db.commit()

    db.refresh(
        tecnico
    )

    logger.info(
        f"Técnico atualizado: {id}"
    )

    return tecnico


@router.delete(
    "/{id}"
)
def excluir_tecnico(
    id: int,
    db: Session = Depends(get_db)
):

    tecnico = db.query(
        Tecnico
    ).filter(
        Tecnico.id == id
    ).first()

    if not tecnico:
        raise HTTPException(
            status_code=404,
            detail="Técnico não encontrado"
        )

    db.delete(
        tecnico
    )

    db.commit()

    logger.info(
        f"Técnico excluído: {id}"
    )

    return {
        "mensagem": "Técnico excluído com sucesso"
    }