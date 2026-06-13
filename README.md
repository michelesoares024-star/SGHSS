# SGHSS — Sistema de Gestão Hospitalar e de Serviços de Saúde

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Swagger/OpenAPI
- Git

---

## Entidades

### Paciente
- id
- nome
- cpf
- telefone
- email
- endereco
- data_nascimento

### Médico
- id
- nome
- crm
- especialidade
- telefone
- email

### Consulta
- id
- data
- observacao
- paciente_id
- medico_id

### Prescrição
- id
- data
- medicamento
- orientacoes
- consulta_id

### Teleconsulta
- id
- teleconsulta
- link
- consulta_id

---

## DER

PACIENTE (1)
↓
CONSULTA (N)

MEDICO (1)
↓
CONSULTA (N)

CONSULTA (1)
↓
PRESCRICAO (N)

CONSULTA (1)
↓
TELECONSULTA (N)

---

## Funcionalidades

- Cadastro de pacientes
- Cadastro de médicos
- Gestão de consultas
- Prescrição digital (MVP)
- Telemedicina (MVP)
- Logs e auditoria
- API REST documentada

---

## Como executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar:

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```