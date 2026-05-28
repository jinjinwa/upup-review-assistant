#!/usr/bin/env bash
set -euo pipefail

export COMPOSE_PROJECT_NAME=upup-open-source
docker compose up -d db redis
cd backend
export DATABASE_URL="${DATABASE_URL:-postgresql+psycopg2://upup:upup_demo_password@localhost:15432/upup_community}"
export REDIS_URL="${REDIS_URL:-redis://localhost:16379/0}"
export CELERY_BROKER_URL="${CELERY_BROKER_URL:-redis://localhost:16379/1}"
export CELERY_RESULT_BACKEND="${CELERY_RESULT_BACKEND:-redis://localhost:16379/2}"
python -m alembic upgrade head
python init_db.py
uvicorn app.main:app --reload --host 0.0.0.0 --port 18000
