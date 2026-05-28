"""Toy scoring for the public demo.

The routine uses only synthetic fields and is intentionally simple.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable

from .demo_data import SAMPLE_MARKET

LATEST_REPORT = {
    "status": "empty",
    "message": "No mock review has been run yet.",
    "items": [],
}


def _score_item(item: dict) -> dict:
    label_bonus = len(item["labels"]) * 7
    activity_bonus = item["demo_activity"] * 4
    volatility_penalty = item["demo_volatility"] * 3
    score = max(1, min(99, 35 + label_bonus + activity_bonus - volatility_penalty))

    if score >= 78:
        band = "Demo Focus"
    elif score >= 62:
        band = "Demo Watch"
    else:
        band = "Demo Observe"

    return {
        "demo_code": item["demo_code"],
        "name": item["name"],
        "theme": item["theme"],
        "toy_score": score,
        "band": band,
        "summary": (
            f"{item['name']} receives a toy score of {score}. "
            f"This is based only on synthetic tags, activity, and volatility fields."
        ),
    }


def run_mock_review(selected_codes: Iterable[str] | None = None) -> dict:
    selected = set(selected_codes or [])
    source_items = [
        item for item in SAMPLE_MARKET if not selected or item["demo_code"] in selected
    ]
    ranked_items = sorted(
        (_score_item(item) for item in source_items),
        key=lambda item: item["toy_score"],
        reverse=True,
    )

    report = {
        "status": "completed",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "item_count": len(ranked_items),
        "items": ranked_items,
        "demo_summary": (
            "Mock review complete. Results are generated from artificial sample "
            "data and toy scoring rules for demonstration only."
        ),
    }
    LATEST_REPORT.clear()
    LATEST_REPORT.update(report)
    return report


def get_latest_report() -> dict:
    return dict(LATEST_REPORT)
