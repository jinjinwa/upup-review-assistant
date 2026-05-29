# UPUP Review Assistant Community Edition

Open-core community scaffold for the UPUP A-share review assistant.

This repository is intentionally **not** the full commercial product. It is a runnable architecture scaffold with frontend, backend, PostgreSQL, Redis, Celery, Alembic, authentication, roles, and mock data governance.

## Product Preview

These masked screenshots show the hosted product experience. The community edition in this repository keeps the architecture scaffold and removes the commercial strategy logic.

### Review Dashboard

![UPUP review dashboard](docs/assets/screenshots/product-dashboard.png)

### Limit-Up Ladder

![UPUP limit-up ladder](docs/assets/screenshots/product-ladder.png)

### Theme Rotation

![UPUP theme rotation](docs/assets/screenshots/product-themes.png)

## Quickstart

```bash
docker compose up --build
```

Open:

```text
http://localhost:18080
```

Default accounts:

```text
admin@example.com / admin123456
demo@example.com / demo123456
```

## What You Can Run

- Register and log in.
- Use JWT-protected frontend routes.
- Switch behavior by normal user vs admin role.
- Create fake review reports.
- Run a generic toy scorer.
- View admin user management with an N+1-safe aggregate query.
- Trigger a mock data source sync through Celery + Redis.
- Inspect SQLAlchemy models and Alembic migration.

## Isolation From the Private App

The community edition is isolated from the private app. It uses its own Compose project, network, volume, and host ports:

```text
project:  upup-open-source
frontend: http://localhost:18080
backend:  http://localhost:18000
postgres: localhost:15432
redis:    localhost:16379
```

It must not stop, reuse, or depend on the private app services.

## What Is Removed

- Production stock pool algorithms.
- Real scoring factors and weights.
- Backtest logic and portfolio logic.
- Real market data integrations.
- Tushare implementation, tokens, field mapping, or sync scripts.
- Commercial membership, payment, card key, and admin business flows.
- Production deployment and infrastructure topology.

## Commercial Product

For the full product, visit [https://upup.live/](https://upup.live/).

Start here: [https://upup.live/register?invite=INV-0E08A](https://upup.live/register?invite=INV-0E08A)

Business contact: 1419995247@qq.com

## Notice

All demo data is synthetic. The generic scorer is a technical scaffold, not a production investment model. Nothing in this repository constitutes investment advice.

## Documentation

- [Quickstart](docs/quickstart.md)
- [Product Preview](docs/product-preview.md)
- [Development Guide](docs/development.md)
- [Architecture](docs/architecture.md)
- [Auth and Roles](docs/auth-and-roles.md)
- [Data Governance](docs/data-governance.md)
- [Task Architecture](docs/task-architecture.md)
- [Scoring Framework](docs/scoring-framework.md)
- [Open-Core Boundary](docs/open-core-boundary.md)
- [Demo Data](docs/demo-data.md)

## License

MIT
