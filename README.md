SGHSS – Sistema de Gestão Hospitalar e de Serviços de Saúde
Descrição do Projeto

O SGHSS (Sistema de Gestão Hospitalar e de Serviços de Saúde) foi desenvolvido como projeto acadêmico com o objetivo de centralizar o gerenciamento de pacientes, profissionais de saúde, consultas, exames, prontuários e telemedicina.

O sistema foi construído utilizando Python, FastAPI, SQLAlchemy e SQLite, seguindo uma arquitetura modular baseada em APIs REST, com documentação automática via Swagger/OpenAPI.

Tecnologias Utilizadas:
Python
FastAPI
SQLAlchemy
SQLite
Swagger/OpenAPI
Git
GitHub
Entidades Implementadas
Pacientes
id
nome
cpf
telefone
email
endereco
data_nascimento
Médicos
id
nome
crm
especialidade
telefone
email
Enfermeiros
id
nome
coren
telefone
email
Técnicos
id
nome
registro
telefone
email
Consultas
id
data
observacao
paciente_id
medico_id
Prescrições
id
data
medicamento
orientacoes
consulta_id
Teleconsultas
id
teleconsulta
link
consulta_id
Prontuários
id
paciente_id
historico_clinico
alergias
created_at
Exames
id
tipo
resultado
data
paciente_id
Diagrama Entidade Relacionamento (DER)
PACIENTE (1)
│
└── CONSULTA (N)

MEDICO (1)
│
└── CONSULTA (N)

CONSULTA (1)
│
├── PRESCRICAO (N)
│
└── TELECONSULTA (N)

PACIENTE (1)
│
├── PRONTUARIO (1)
│
└── EXAME (N)

O DER visual encontra-se disponível na pasta docs/DER_SGHSS.png.

Funcionalidades Implementadas:
Gestão de Pacientes
Cadastro de pacientes
Consulta de pacientes
Atualização de pacientes
Exclusão de pacientes
Histórico clínico
Gestão de Médicos
Cadastro de médicos
Consulta de médicos
Atualização de médicos
Exclusão de médicos
Agenda médica
Gestão de Enfermeiros
Cadastro e consulta de enfermeiros
Gestão de Técnicos
Cadastro e consulta de técnicos
Gestão de Consultas
Agendamento de consultas
Atualização de consultas
Cancelamento de consultas
Gestão de Prontuários
Cadastro de prontuários
Histórico clínico do paciente
Gestão de Exames
Cadastro de exames
Consulta de exames
Gestão de Prescrições
Registro de prescrições médicas
Telemedicina
Registro de teleconsultas
Associação com consultas médicas
Auditoria e Monitoramento
Registro de logs
Auditoria básica de operações
Endpoint de monitoramento (/health)
Segurança e LGPD

O SGHSS foi desenvolvido seguindo princípios básicos da Lei Geral de Proteção de Dados (LGPD).

Medidas Implementadas
Registro de logs para auditoria.
Tratamento de erros utilizando HTTPException.
Organização modular do projeto.
Separação entre Models, Schemas e APIs.
Controle de integridade dos dados através do banco SQLite.
Estrutura preparada para futura implementação de autenticação e autorização.
Limitações da Versão Acadêmica
Não possui autenticação de usuários.
Não possui criptografia avançada de dados sensíveis.
Não possui gestão de consentimento dos titulares.
Não possui anonimização de dados.
Não possui controle de acesso por perfil.

Como Executar o Projeto:
Instalar Dependências
pip install -r requirements.txt

Executar a Aplicação
uvicorn app.main:app --reload

Documentação Swagger
http://127.0.0.1:8000/docs

Health Check
http://127.0.0.1:8000/health
Estrutura do Projeto
app/
├── api/
├── core/
├── models/
├── schemas/
├── main.py

docs/
└── DER_SGHSS.png

README.md
requirements.txt

Funcionalidades Futuras:
Controle de acesso por perfil.
Gestão de leitos hospitalares.
Gestão financeira hospitalar.
Gestão de suprimentos.
Integração com videochamadas.
Criptografia avançada de dados.
Adequação completa à LGPD.
Dashboard administrativo.
Multiunidades hospitalares.

Autor
Michele Tamiosso Soares
Projeto desenvolvido para fins acadêmicos na disciplina de Desenvolvimento Back-end.