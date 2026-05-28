#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "uvicorn" ]]; then
  alembic upgrade head
  python init_db.py
fi

exec "$@"
