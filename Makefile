.PHONY: start stop restart logs test backend-test frontend-build

start:
	COMPOSE_PROJECT_NAME=upup-open-source docker compose up --build

stop:
	COMPOSE_PROJECT_NAME=upup-open-source docker compose down

restart:
	COMPOSE_PROJECT_NAME=upup-open-source docker compose down && COMPOSE_PROJECT_NAME=upup-open-source docker compose up --build

logs:
	COMPOSE_PROJECT_NAME=upup-open-source docker compose logs -f

backend-test:
	cd backend && python -m pytest

frontend-build:
	cd frontend && npm run build

test: backend-test frontend-build
