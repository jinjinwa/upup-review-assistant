from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models import DemoReport, User
from app.schemas.scoring import ScoreDimension, ScoreRequest
from app.services.scoring import evaluate_score


def create_demo_review(db: Session, user: User) -> DemoReport:
    result = evaluate_score(
        ScoreRequest(
            title="社区版复盘骨架评分",
            dimensions=[
                ScoreDimension(name="data_completeness", value=78, weight=0.35),
                ScoreDimension(name="workflow_readiness", value=84, weight=0.4),
                ScoreDimension(name="demo_volatility", value=62, weight=0.25),
            ],
        )
    )
    report = DemoReport(
        user_id=user.id,
        title=result.title,
        score=result.score,
        summary="这是一条社区版 fake report，用于展示复盘工作流骨架，不包含真实策略。",
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


def list_reports(db: Session, user: User) -> list[DemoReport]:
    stmt = (
        select(DemoReport)
        .where(DemoReport.user_id == user.id)
        .order_by(desc(DemoReport.created_at))
        .limit(20)
    )
    return list(db.scalars(stmt))
