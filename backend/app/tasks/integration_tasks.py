from datetime import datetime, timezone
from time import sleep

from sqlalchemy import select

from app.celery_app import celery_app
from app.core.database import SessionLocal
from app.models import DataSource, IntegrationRun


@celery_app.task(name="community.fake_data_source_sync")
def run_fake_data_source_sync(run_id: int) -> dict:
    db = SessionLocal()
    try:
        run = db.scalar(select(IntegrationRun).where(IntegrationRun.id == run_id))
        if run is None:
            return {"status": "missing", "run_id": run_id}

        run.status = "running"
        run.started_at = datetime.now(timezone.utc)
        run.message = "Mock connector is validating synthetic metadata."
        db.commit()

        sleep(1)

        source = db.scalar(select(DataSource).where(DataSource.id == run.data_source_id))
        if source is not None:
            source.status = "mock_synced"
            source.last_sync_at = datetime.now(timezone.utc)
        run.status = "success"
        run.finished_at = datetime.now(timezone.utc)
        run.message = "Mock sync completed with synthetic task results."
        db.commit()
        return {"status": "success", "run_id": run_id}
    finally:
        db.close()
