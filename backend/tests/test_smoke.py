from fastapi.testclient import TestClient

from app.api import admin as admin_api
from app.core.database import Base, SessionLocal, engine
from app.core.password import hash_password
from app.main import app
from app.models import DataSource, IntegrationRun, User

client = TestClient(app)


def setup_module():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    db.add_all(
        [
            DataSource(name="Mock Market Snapshot", kind="synthetic-file"),
            DataSource(name="Mock Fundamentals Feed", kind="synthetic-api"),
        ]
    )
    db.commit()
    db.close()


def register_and_login(email: str = "case@example.com", role_path: str = "user"):
    client.post(
        "/api/auth/register",
        json={"username": role_path, "email": email, "password": "password123"},
    )
    response = client.post("/api/auth/login", json={"email": email, "password": "password123"})
    assert response.status_code == 200
    return response.json()["data"]["access_token"]


def create_seed_user(email: str, username: str, role: str = "user", is_active: bool = True) -> str:
    db = SessionLocal()
    try:
        user = User(
            username=username,
            email=email,
            password_hash=hash_password("password123"),
            role=role,
            is_active=is_active,
        )
        db.add(user)
        db.commit()
    finally:
        db.close()
    if not is_active:
        return ""
    response = client.post("/api/auth/login", json={"email": email, "password": "password123"})
    assert response.status_code == 200
    return response.json()["data"]["access_token"]


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["data"]["status"] == "ok"


def test_auth_review_and_scoring_cycle():
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}

    overview = client.get("/api/demo/overview", headers=headers)
    assert overview.status_code == 200

    review = client.post("/api/demo/reviews", headers=headers)
    assert review.status_code == 200
    assert review.json()["data"]["score"] > 0

    scoring = client.post(
        "/api/scoring/evaluate",
        headers=headers,
        json={
            "title": "generic",
            "dimensions": [
                {"name": "completeness", "value": 80, "weight": 0.5},
                {"name": "workflow", "value": 70, "weight": 0.5},
            ],
        },
    )
    assert scoring.status_code == 200
    assert scoring.json()["data"]["score"] == 75


def test_admin_guard_blocks_normal_user():
    token = register_and_login("normal@example.com", "normal")
    response = client.get("/api/admin/users", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403


def test_inactive_user_cannot_login():
    create_seed_user("inactive@example.com", "inactive", is_active=False)
    response = client.post(
        "/api/auth/login",
        json={"email": "inactive@example.com", "password": "password123"},
    )
    assert response.status_code == 401


def test_admin_sync_returns_structured_error_when_queue_unavailable(monkeypatch):
    token = create_seed_user("admin-sync@example.com", "admin-sync", role="admin")

    def fail_delay(_: int):
        raise RuntimeError("broker offline")

    monkeypatch.setattr(admin_api.run_fake_data_source_sync, "delay", fail_delay)
    response = client.post(
        "/api/admin/data-sources/1/sync",
        headers={"Authorization": f"Bearer {token}"},
    )
    payload = response.json()
    assert response.status_code == 503
    assert payload["success"] is False
    assert payload["code"] == 503

    db = SessionLocal()
    try:
        run = db.query(IntegrationRun).order_by(IntegrationRun.id.desc()).first()
        assert run is not None
        assert run.status == "failed"
    finally:
        db.close()
