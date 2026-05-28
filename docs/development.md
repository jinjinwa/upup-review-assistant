# Development Guide

## Scripts

```bash
bash scripts/dev-infra.sh
bash scripts/dev-backend.sh
bash scripts/dev-frontend.sh
bash scripts/dev-fullstack.sh
bash scripts/prod-start.sh
```

All scripts set `COMPOSE_PROJECT_NAME=upup-open-source` and use isolated host ports:

```text
frontend 18080
backend  18000
postgres 15432
redis    16379
```

## Tests

```bash
cd backend && python -m pytest
cd frontend && npm run build
```

## Database

Schema changes go through Alembic:

```bash
cd backend
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

The Docker backend entrypoint runs migrations and then `init_db.py`.

This repository intentionally does not ship a data-wiping helper. Stop services with `docker compose down`; remove volumes only if you explicitly understand the local data impact.
