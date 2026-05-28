#!/usr/bin/env bash
set -euo pipefail

export COMPOSE_PROJECT_NAME=upup-open-source
docker compose up -d db redis
