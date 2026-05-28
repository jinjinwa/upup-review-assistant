from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "upup_community",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
    include=["app.tasks.integration_tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Shanghai",
    enable_utc=True,
)
