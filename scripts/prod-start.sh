#!/usr/bin/env bash
set -euo pipefail

export COMPOSE_PROJECT_NAME=stock-quant-review-assistant
docker compose up --build -d
docker compose ps
