from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .demo_data import get_market_snapshot
from .demo_scoring import get_latest_report
from .demo_tasks import get_task, submit_review_task

APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"

app = FastAPI(
    title="UPUP Review Assistant Demo",
    version="0.1.0",
    description="Minimal runnable demo with synthetic data and toy scoring.",
)


class ReviewRequest(BaseModel):
    selected_codes: list[str] = Field(default_factory=list)


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "demo": True}


@app.get("/api/demo/market")
def demo_market():
    return get_market_snapshot()


@app.post("/api/demo/review")
def demo_review(payload: ReviewRequest | None = None):
    selected_codes = payload.selected_codes if payload else []
    return submit_review_task(selected_codes)


@app.get("/api/demo/report")
def demo_report():
    return get_latest_report()


@app.get("/api/demo/tasks/{task_id}")
def demo_task(task_id: str):
    task = get_task(task_id)
    if task is None:
        return {"task_id": task_id, "status": "missing"}
    return task


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
