#!/usr/bin/env bash
set -euo pipefail

export COMPOSE_PROJECT_NAME=stock-quant-review-assistant
docker compose up -d db redis backend celery-worker
cd frontend
npm ci
npm run dev -- --host 0.0.0.0 --port 18080
