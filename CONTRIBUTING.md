# Contributing

Thank you for your interest in the UPUP Review Assistant Demo.

## Scope

Contributions should improve the public demo experience, documentation, tests, or local setup. Keep all examples synthetic.

## Before Opening a Pull Request

- Run `python -m pytest` in the backend directory.
- Run `docker compose up --build` from the repository root.
- Confirm the demo opens at `http://localhost:8080`.
- Confirm no private credentials or real data are included.

## Demo Boundary

Please do not add real market data, production scoring logic, production deployment details, user systems, payment systems, or admin features.
