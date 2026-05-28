# Quickstart

```bash
docker compose up --build
```

Open `http://localhost:18080`.

Default accounts:

```text
admin@example.com / admin123456
demo@example.com / demo123456
```

Useful endpoints:

```text
GET  /api/health
POST /api/auth/login
GET  /api/auth/me
POST /api/demo/reviews
GET  /api/admin/data-sources
POST /api/admin/data-sources/{id}/sync
```
