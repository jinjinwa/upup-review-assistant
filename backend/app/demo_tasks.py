"""In-memory task abstraction for demo review runs."""

from __future__ import annotations

from itertools import count

from .demo_scoring import run_mock_review

_task_counter = count(1)
_tasks: dict[str, dict] = {}


def submit_review_task(selected_codes: list[str] | None = None) -> dict:
    task_id = f"demo-task-{next(_task_counter):04d}"
    _tasks[task_id] = {"task_id": task_id, "status": "processing"}
    report = run_mock_review(selected_codes)
    _tasks[task_id] = {
        "task_id": task_id,
        "status": "completed",
        "report": report,
    }
    return _tasks[task_id]


def get_task(task_id: str) -> dict | None:
    return _tasks.get(task_id)
