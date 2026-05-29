# Task Architecture

Celery and Redis are included so the community edition can demonstrate asynchronous task processing.

```mermaid
flowchart LR
  API["FastAPI admin API"] --> Run["integration_runs row"]
  API --> Queue["Redis broker"]
  Queue --> Worker["Celery worker"]
  Worker --> DB["PostgreSQL status update"]
```

The task name is `community.fake_data_source_sync`. It is a mock task for local task-flow demos.
