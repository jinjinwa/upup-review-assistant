from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_market_uses_synthetic_entries():
    response = client.get("/api/demo/market")
    payload = response.json()
    assert response.status_code == 200
    assert payload["source"] == "synthetic"
    assert payload["count"] == 5
    assert payload["items"][0]["demo_code"].startswith("DEMO")


def test_review_and_report_cycle():
    review = client.post("/api/demo/review", json={"selected_codes": []})
    assert review.status_code == 200
    review_payload = review.json()
    assert review_payload["status"] == "completed"
    assert review_payload["report"]["item_count"] == 5
    assert "toy_score" in review_payload["report"]["items"][0]

    report = client.get("/api/demo/report")
    assert report.status_code == 200
    assert report.json()["status"] == "completed"
