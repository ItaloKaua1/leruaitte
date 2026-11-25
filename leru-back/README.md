# Leruaite — Back-end

API do Leruaite, feita com FastAPI, WebSockets, SQLAlchemy, Alembic e PostgreSQL. A autenticação usa JWT.

## Pré-requisitos

- Python 3.11 ou superior
- Docker, para subir o PostgreSQL

## Como rodar localmente

Todos os comandos abaixo, exceto o passo 4, são executados dentro de `leru-back/`.

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente:

| Sistema | Comando |
| --- | --- |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (Git Bash) | `source .venv/Scripts/activate` |
| Linux/macOS | `source .venv/bin/activate` |

### 2. Instalar as dependências

```bash
pip install -r requirements-dev.txt
```

O `requirements-dev.txt` inclui as dependências da aplicação e as de teste (pytest e httpx).

### 3. Configurar as variáveis de ambiente

```bash
cp .env.example .env
```

| Variável | Descrição |
| --- | --- |
| `DATABASE_URL` | URL de conexão com o PostgreSQL |
| `JWT_SECRET_KEY` | Chave para assinar os tokens (use 32 caracteres ou mais e troque em produção) |
| `JWT_ALGORITHM` | Algoritmo do JWT (padrão `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Validade do token, em minutos |
| `CORS_ORIGINS` | Origens liberadas no CORS, em formato JSON |

### 4. Subir o PostgreSQL

Na raiz do projeto (`leruaite/`):

```bash
docker compose up -d db
```

O banco fica disponível em `localhost:5432`. Usuário, senha e nome do banco são `leruaite`.

### 5. Aplicar as migrações

```bash
alembic upgrade head
```

### 6. Iniciar a API

```bash
fastapi dev app/main.py
```

O servidor recarrega sozinho quando o código muda.

- API: http://localhost:8000
- Documentação interativa: http://localhost:8000/docs
- Health check: http://localhost:8000/health
- WebSocket de exemplo: `ws://localhost:8000/ws`

## Testes

```bash
pytest
```

## Migrações

Para criar uma migração depois de adicionar ou alterar um model:

1. Importe o model em `app/db/base.py`, para que o Alembic o detecte.
2. Gere a migração:

   ```bash
   alembic revision --autogenerate -m "descricao da mudanca"
   ```

3. Revise o arquivo gerado em `alembic/versions/`.
4. Aplique a migração:

   ```bash
   alembic upgrade head
   ```

Para desfazer a última migração: `alembic downgrade -1`

## Rodando com Docker

Na raiz do projeto, o comando abaixo sobe o banco, a API e o front-end:

```bash
docker compose up --build
```

O container da API aplica as migrações antes de iniciar o servidor.

## Estrutura

```
leru-back/
├── app/
│   ├── api/          # Rotas HTTP e WebSocket
│   ├── core/         # Configurações e segurança (JWT, hash de senha)
│   ├── db/           # Base dos models e sessão do SQLAlchemy
│   └── main.py       # Criação da aplicação FastAPI
├── alembic/          # Migrações do banco
├── tests/            # Testes com pytest
├── alembic.ini
├── Dockerfile
├── requirements.txt
└── requirements-dev.txt
```
