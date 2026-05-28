from fastapi.testclient import TestClient

from app.core.database import Base, SessionLocal, engine
from app.main import app
from app.models import DataSource

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
