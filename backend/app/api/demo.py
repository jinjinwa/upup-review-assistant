from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.core.database import get_db
from app.core.response import success_response
from app.models import User
from app.services.demo_service import create_demo_review, list_reports

router = APIRouter(prefix="/api/demo", tags=["demo"])


@router.get("/overview")
def overview(user: User = Depends(get_current_user)):
    return success_response(
        {
            "welcome": f"Welcome, {user.username}",
            "role": user.role,
            "modules": [
                "Demo dashboard",
                "Generic scorer",
                "Fake reports",
                "Admin data governance" if user.role == "admin" else "User workspace",
            ],
            "notice": "Synthetic community edition data only.",
        }
    )


@router.post("/reviews")
def create_review(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    report = create_demo_review(db, user)
    return success_response(
        {
            "id": report.id,
            "title": report.title,
            "score": report.score,
            "summary": report.summary,
            "created_at": str(report.created_at),
        },
        message="Demo review created",
    )


@router.get("/reports")
def reports(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    items = [
        {
            "id": item.id,
            "title": item.title,
            "score": item.score,
            "summary": item.summary,
            "created_at": str(item.created_at),
        }
        for item in list_reports(db, user)
    ]
    return success_response({"items": items})
