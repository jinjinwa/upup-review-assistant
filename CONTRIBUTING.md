# Contributing

Contributions are welcome when they improve the community scaffold.

## Scope

Accepted:

- Developer experience improvements.
- Auth, role, database, task, or frontend scaffold improvements.
- Synthetic demo pages and docs.
- Tests and local setup fixes.

Out of scope:

- Real market data integrations.
- Production scoring factors or strategies.
- Backtest engines.
- Membership, payment, card key, or commercial permission flows.
- Production infrastructure details.

## Checks

```bash
cd backend && python -m pytest
cd frontend && npm run build
docker compose up --build
```
