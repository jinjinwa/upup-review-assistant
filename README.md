# UPUP Review Assistant Community Edition

Runnable open-core community edition for the UPUP A-share review assistant.

This repository gives developers a complete local product scaffold: React frontend, FastAPI backend, PostgreSQL, Redis, Celery, Alembic, authentication, roles, admin views, demo data workflows, and documentation.

## Product Preview

These masked screenshots show the hosted UPUP product experience. The community edition gives you the runnable foundation behind that direction, with safe demo workflows you can run locally.

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
project:  upup-open-source
frontend: http://localhost:18080
backend:  http://localhost:18000
postgres: localhost:15432
redis:    localhost:16379
```

Run it independently from any other local services.

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
- [Community Scope](docs/community-scope.md)
- [Demo Data](docs/demo-data.md)

## License

MIT
