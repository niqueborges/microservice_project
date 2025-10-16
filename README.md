# Microservice Project — FastAPI + PostgreSQL

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.1-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

Microserviço em Python usando **FastAPI** e **PostgreSQL**, com **SQLAlchemy** e boas práticas de arquitetura para microserviços.
Projeto serve como base para aprendizado e desenvolvimento de APIs escaláveis.

---

## 🗂 Estrutura do projeto

```
microservice_project/
│
├─ app/
│   ├─ main.py            # Entrypoint do microserviço
│   ├─ models.py          # Modelos SQLAlchemy
│   ├─ schemas.py         # Schemas Pydantic
│   ├─ crud.py            # Funções CRUD
│   ├─ database.py        # Conexão com PostgreSQL
│   └─ routers/
│       └─ users.py       # Endpoints relacionados a usuários
│
├─ .env                   # Variáveis de ambiente (credenciais)
├─ requirements.txt       # Dependências do Python
└─ README.md              # Este arquivo
```

---

## ⚙️ Configuração

1. Crie o arquivo `.env` na raiz do projeto:

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=microservice_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

> Substitua `user`, `password` e `microservice_db` pelas credenciais do seu PostgreSQL.

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Certifique-se que o PostgreSQL está rodando e que o banco existe.

---

## 🏗 Executar o microserviço

```bash
uvicorn app.main:app --reload
```

* Acesse a documentação automática do Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔹 Boas práticas implementadas

* Uso de **.env** para variáveis sensíveis
* Estrutura modular com `routers`, `models`, `schemas`, `crud`
* Documentação automática do FastAPI
* Conexão segura e configurável com PostgreSQL

---

## 🔹 Próximos passos sugeridos

* Dockerizar microserviço com PostgreSQL
* Criar testes automatizados (pytest)
* Versionar API (`/v1/users`)
* Adicionar logging estruturado

---

## 📚 Referências

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
* [PostgreSQL Documentation](https://www.postgresql.org/docs/)
