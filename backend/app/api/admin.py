from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.exceptions import NotFoundException
from app.core.permissions import require_admin
from app.core.response import success_response
from app.models import DataSource, DemoReport, IntegrationRun, User
from app.tasks.integration_tasks import run_fake_data_source_sync

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/users")
def users(_: User = Depends(require_admin), db: Session = Depends(get_db)):
    report_counts = (
        select(DemoReport.user_id, func.count(DemoReport.id).label("report_count"))
        .group_by(DemoReport.user_id)
        .subquery()
    )
    stmt = (
        select(User, func.coalesce(report_counts.c.report_count, 0))
        .outerjoin(report_counts, User.id == report_counts.c.user_id)
        .order_by(User.id)
    )
    rows = db.execute(stmt).all()
    return success_response(
        {
            "items": [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "is_active": user.is_active,
                    "report_count": report_count,
                }
                for user, report_count in rows
            ],
            "implementation_note": "Report counts are loaded with one aggregate query to avoid N+1 lookups.",
        }
    )


@router.get("/data-sources")
def data_sources(_: User = Depends(require_admin), db: Session = Depends(get_db)):
    sources = list(db.scalars(select(DataSource).order_by(DataSource.id)))
    return success_response(
        {
            "items": [
                {
                    "id": source.id,
                    "name": source.name,
                    "kind": source.kind,
                    "status": source.status,
                    "is_enabled": source.is_enabled,
                    "last_sync_at": str(source.last_sync_at) if source.last_sync_at else None,
                }
                for source in sources
            ]
        }
    )


@router.post("/data-sources/{source_id}/sync")
def sync_data_source(
    source_id: int,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    source = db.scalar(select(DataSource).where(DataSource.id == source_id))
    if source is None:
        raise NotFoundException("Data source not found")

    run = IntegrationRun(
        data_source_id=source.id,
        status="queued",
        message="Queued mock sync task.",
        started_at=datetime.now(timezone.utc),
    )
    db.add(run)
    db.commit()
    db.refresh(run)
    run_fake_data_source_sync.delay(run.id)
    return success_response({"task_id": run.id, "status": run.status}, message="Mock sync queued")


@router.get("/tasks")
def tasks(_: User = Depends(require_admin), db: Session = Depends(get_db)):
    stmt = select(IntegrationRun).order_by(desc(IntegrationRun.created_at)).limit(30)
    runs = list(db.scalars(stmt))
    return success_response(
        {
            "items": [
                {
                    "id": run.id,
                    "data_source_id": run.data_source_id,
                    "status": run.status,
                    "message": run.message,
                    "created_at": str(run.created_at),
                    "finished_at": str(run.finished_at) if run.finished_at else None,
                }
                for run in runs
            ]
        }
    )
