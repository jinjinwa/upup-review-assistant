#!/usr/bin/env bash
set -euo pipefail

export COMPOSE_PROJECT_NAME=upup-open-source
docker compose up -d db redis backend celery-worker
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 18080
