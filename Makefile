.PHONY: start stop restart logs test backend-test frontend-build

start:
	COMPOSE_PROJECT_NAME=stock-quant-review-assistant docker compose up --build

stop:
	COMPOSE_PROJECT_NAME=stock-quant-review-assistant docker compose down

restart:
	COMPOSE_PROJECT_NAME=stock-quant-review-assistant docker compose down && COMPOSE_PROJECT_NAME=stock-quant-review-assistant docker compose up --build

logs:
	COMPOSE_PROJECT_NAME=stock-quant-review-assistant docker compose logs -f

backend-test:
	cd backend && python3 -m pytest

frontend-build:
	cd frontend && npm ci && npm run build

test: backend-test frontend-build
