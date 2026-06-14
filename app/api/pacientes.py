from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger
from app.models.paciente import Paciente
from app.models.consulta import Consulta
from app.models.prontuario import Prontuario
from app.models.exame import Exame
from app.schemas.paciente import (
    PacienteCreate,
    PacienteResponse
)

router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"]
)


@router.get(
    "/",
    response_model=list[PacienteResponse]
)
def listar_pacientes(
    db: Session = Depends(get_db)
):
    return db.query(Paciente).all()



@router.get(
    "/{id}",
    response_model=PacienteResponse
)
def buscar_paciente(
    id: int,
    db: Session = Depends(get_db)
):
    paciente = db.query(Paciente).filter(
        Paciente.id == id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    return paciente

@router.post(
    "/",
    response_model=PacienteResponse,
    status_code=201
)
def criar_paciente(
    paciente: PacienteCreate,
    db: Session = Depends(get_db)
):

    cpf_existente = db.query(Paciente).filter(
        Paciente.cpf == paciente.cpf
    ).first()

    if cpf_existente:
        raise HTTPException(
            status_code=400,
            detail="CPF já cadastrado"
        )
    
    novo_paciente = Paciente(
        nome=paciente.nome,
        cpf=paciente.cpf,
        telefone=paciente.telefone,
        email=paciente.email,
        endereco=paciente.endereco,
        data_nascimento=paciente.data_nascimento
    )

    db.add(novo_paciente)
    db.commit()
    db.refresh(
    novo_paciente
)

    logger.info(
        f"Paciente criado: {novo_paciente.nome}"
)

    return novo_paciente


@router.put(
    "/{id}",
    response_model=PacienteResponse
)
def atualizar_paciente(
    id: int,
    dados: PacienteCreate,
    db: Session = Depends(get_db)
):
    paciente = db.query(Paciente).filter(
        Paciente.id == id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    paciente.nome = dados.nome
    paciente.cpf = dados.cpf
    paciente.telefone = dados.telefone
    paciente.email = dados.email
    paciente.endereco = dados.endereco
    paciente.data_nascimento = dados.data_nascimento

    db.commit()
    db.refresh(paciente)

    return paciente


@router.delete("/{id}")
def excluir_paciente(
    id: int,
    db: Session = Depends(get_db)
):
    paciente = db.query(Paciente).filter(
        Paciente.id == id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    db.delete(paciente)
    db.commit()

    logger.info(
    f"Paciente removido: {paciente.nome}"
    )

    return {
        "mensagem": "Paciente excluído com sucesso"
    }

@router.get(
    "/{id}/consultas"
)
def historico_paciente(
    id: int,
    db: Session = Depends(get_db)
):

    paciente = db.query(
        Paciente
    ).filter(
        Paciente.id == id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    consultas = db.query(
        Consulta
    ).filter(
        Consulta.paciente_id == id
    ).all()

    return consultas

@router.get(
    "/{id}/prontuario"
)
def buscar_prontuario_paciente(
    id: int,
    db: Session = Depends(get_db)
):

    paciente = db.query(Paciente).filter(
        Paciente.id == id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    prontuario = db.query(Prontuario).filter(
        Prontuario.paciente_id == id
    ).first()

    if not prontuario:
        raise HTTPException(
            status_code=404,
            detail="Prontuário não encontrado"
        )

    return prontuario


@router.get(
    "/{id}/exames"
)
def listar_exames_paciente(
    id: int,
    db: Session = Depends(get_db)
):

    paciente = db.query(Paciente).filter(
        Paciente.id == id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    exames = db.query(Exame).filter(
        Exame.paciente_id == id
    ).all()

    return exames


@router.get(
    "/{id}/historico"
)
def historico_completo_paciente(
    id: int,
    db: Session = Depends(get_db)
):

    paciente = db.query(Paciente).filter(
        Paciente.id == id
    ).first()

    if not paciente:
        raise HTTPException(
            status_code=404,
            detail="Paciente não encontrado"
        )

    consultas = db.query(Consulta).filter(
        Consulta.paciente_id == id
    ).all()

    prontuario = db.query(Prontuario).filter(
        Prontuario.paciente_id == id
    ).first()

    exames = db.query(Exame).filter(
        Exame.paciente_id == id
    ).all()

    return {
        "paciente": paciente,
        "consultas": consultas,
        "prontuario": prontuario,
        "exames": exames
    }