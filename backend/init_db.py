from sqlalchemy import select

from app.core.config import settings
from app.core.database import SessionLocal
from app.core.password import hash_password
from app.models import DataSource, DemoReport, User


def ensure_user(db, username: str, email: str, password: str, role: str) -> User:
    user = db.scalar(select(User).where(User.email == email))
    if user is None:
        user = User(
            username=username,
            email=email,
            password_hash=hash_password(password),
            role=role,
            is_active=True,
        )
        db.add(user)
        db.flush()
    else:
        user.role = role
        user.is_active = True
    return user


def seed_data_sources(db) -> None:
    existing = db.scalar(select(DataSource).limit(1))
    if existing:
        return
    db.add_all(
        [
            DataSource(name="Mock Market Snapshot", kind="synthetic-file", status="mock_ready"),
            DataSource(name="Mock Fundamentals Feed", kind="synthetic-api", status="mock_ready"),
            DataSource(name="Mock Quality Rules", kind="rule-pack", status="mock_ready"),
        ]
    )


def seed_reports(db, user: User) -> None:
    existing = db.scalar(select(DemoReport).where(DemoReport.user_id == user.id).limit(1))
    if existing:
        return
    db.add_all(
        [
            DemoReport(
                user_id=user.id,
                title="社区版启动报告",
                score=76,
                summary="Fake report showing a complete user workflow without core strategy logic.",
            ),
            DemoReport(
                user_id=user.id,
                title="通用评分器示例",
                score=82,
                summary="Generic score produced from demo dimensions, not a production stock algorithm.",
            ),
        ]
    )


def main() -> None:
    db = SessionLocal()
    try:
        admin = ensure_user(
            db,
            username="admin",
            email=settings.demo_admin_email,
            password=settings.demo_admin_password,
            role="admin",
        )
        demo_user = ensure_user(
            db,
            username="demo",
            email=settings.demo_user_email,
            password=settings.demo_user_password,
            role="user",
        )
        seed_data_sources(db)
        seed_reports(db, admin)
        seed_reports(db, demo_user)
        db.commit()
        print("Community demo data initialized")
    finally:
        db.close()


if __name__ == "__main__":
    main()
