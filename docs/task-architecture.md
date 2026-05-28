# Task Architecture

Celery and Redis are included so the community edition has the same architectural shape as a production async system.

```mermaid
flowchart LR
  API["FastAPI admin API"] --> Run["integration_runs row"]
  API --> Queue["Redis broker"]
  Queue --> Worker["Celery worker"]
  Worker --> DB["PostgreSQL status update"]
```

The task name is `community.fake_data_source_sync`. It is a mock task and does not contain production queue names or scheduling logic.
