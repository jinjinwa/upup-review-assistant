# Stock Quant Review Assistant Community Edition

Runnable open-core community edition for stock review and quantitative analysis workflows.

This repository gives developers a complete local product scaffold: React frontend, FastAPI backend, PostgreSQL, Redis, Celery, Alembic, authentication, roles, admin views, demo data workflows, and documentation.

Keywords: stock, quant, quantitative finance, stock analysis, A-share review, 股票复盘, 量化选股.

## Hosted Product Access

Use the invite link to experience the deployed version with hosted permissions: [https://upup.live/register?invite=INV-0E08A](https://upup.live/register?invite=INV-0E08A)

## Product Preview

These screenshots show the community edition running locally with synthetic demo data.

### Community Dashboard

![Stock Quant community dashboard](docs/assets/screenshots/community-dashboard.png)

### Demo Review

![Stock Quant demo review](docs/assets/screenshots/community-review.png)

### Admin Data Governance

![Stock Quant admin data governance](docs/assets/screenshots/community-admin-data.png)

## Quickstart

```bash
make start
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

## Community Edition Includes

- Register and log in.
- Use JWT-protected frontend routes.
- Switch behavior by normal user vs admin role.
- Create fake review reports.
- Run a generic example scorer.
- View admin user management with an N+1-safe aggregate query.
- Trigger a mock data source sync through Celery + Redis.
- Inspect SQLAlchemy models and Alembic migration.
- Extend the app shell, API contracts, worker tasks, and database models for your own scenarios.

## Standalone Runtime

The community edition runs as a standalone Compose project with its own network, volume, and host ports:

```text
project:  stock-quant-review-assistant
frontend: http://localhost:18080
backend:  http://localhost:18000
postgres: localhost:15432
redis:    localhost:16379
```

Run it independently from any other local services.

## Business Inquiries

Business contact: 1419995247@qq.com

## Notice

All demo data is synthetic. The generic scorer is a technical scaffold for local development. Nothing in this repository constitutes investment advice.

## Documentation

- [Quickstart](docs/quickstart.md)
- [Product Preview](docs/product-preview.md)
- [Development Guide](docs/development.md)
- [Architecture](docs/architecture.md)
- [Auth and Roles](docs/auth-and-roles.md)
- [Data Governance](docs/data-governance.md)
- [Task Architecture](docs/task-architecture.md)
- [Scoring Framework](docs/scoring-framework.md)
- [Community Scope](docs/community-scope.md)
- [Demo Data](docs/demo-data.md)

## License

MIT
