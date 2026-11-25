# Leruaite — Back-end

FastAPI + PostgreSQL. Requer Python 3.11+ e Docker.

## Rodando localmente

Dentro de `leru-back/`:

```bash
python -m venv .venv
```

Ative o ambiente:

| Sistema | Comando |
| --- | --- |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (Git Bash) | `source .venv/Scripts/activate` |
| Linux/macOS | `source .venv/bin/activate` |

```bash
pip install -r requirements-dev.txt
cp .env.example .env
docker compose up -d db     # sobe o Postgres
alembic upgrade head
fastapi dev app/main.py
```

API em http://localhost:8000. Documentação em http://localhost:8000/docs.

## Comandos úteis

| Ação | Comando |
| --- | --- |
| Rodar os testes | `pytest` |
| Criar migração | `alembic revision --autogenerate -m "descricao"` |
| Aplicar migrações | `alembic upgrade head` |
| Desfazer a última migração | `alembic downgrade -1` |
| Subir tudo (banco, API e front) | `docker compose up --build` |

Para o Alembic detectar um model novo, importe-o em `app/db/base.py`.
