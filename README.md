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

Segurança e LGPD

O SGHSS foi desenvolvido seguindo princípios básicos da Lei Geral de Proteção de Dados (LGPD).

Medidas implementadas:

Registro de logs para auditoria.
Controle de integridade dos dados através do banco SQLite.
Organização modular para futura implementação de autenticação e autorização.
Separação entre modelos, schemas e APIs.
Tratamento de erros utilizando HTTPException.

Limitações da versão acadêmica:

Não possui autenticação por usuário.
Não possui criptografia avançada de dados sensíveis.
Não possui gestão de consentimento dos titulares.
Não possui anonimização de dados.

Essas funcionalidades podem ser implementadas em versões futuras do sistema.

Funcionalidades Futuras
Controle de acesso por perfil.
Gestão de leitos hospitalares.
Controle financeiro.
Gestão de suprimentos.
Integração com serviços de telemedicina.
Criptografia avançada de dados.
Adequação completa à LGPD.
Dashboard administrativo.
Multiunidades hospitalares.