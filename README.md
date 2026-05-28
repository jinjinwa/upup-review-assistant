# UPUP Review Assistant Demo

Runnable minimal demo for an A-share review assistant concept.

This repository is a public open-source demo, not the complete UPUP product. It contains only synthetic sample data, a toy scoring routine, and a small FastAPI web page that can run locally.

## Try It

```bash
docker compose up --build
```

Open:

```text
http://localhost:8080
```

The page loads synthetic demo entries, runs one mock review, and displays a toy score with a short demo summary.

## What Is Included

- A FastAPI backend.
- A static demo page.
- Fully artificial sample data.
- Toy scoring based on demo-only fields such as tag count, activity level, and demo volatility.
- Documentation for the public demo boundary.

## What Is Not Included

- The complete commercial product.
- Production scoring logic.
- Real market data, real securities data, or historical returns.
- User systems, subscriptions, payments, admin features, or production deployment assets.

## Commercial Product

For the full product, visit [https://upup.live/](https://upup.live/).

Start here: [https://upup.live/register?invite=INV-0E08A](https://upup.live/register?invite=INV-0E08A)

Business contact: 1419995247@qq.com

## Important Notice

The sample data in this repository is completely artificial. The toy scoring routine is only for demonstrating a local workflow. This repository does not provide investment advice.

## Documentation

- [Quickstart](docs/quickstart.md)
- [Architecture](docs/architecture.md)
- [Task Architecture](docs/task-architecture.md)
- [Open-Core Boundary](docs/open-core-boundary.md)
- [Demo Data](docs/demo-data.md)

## License

MIT
