"""Tests for the foundation HTTP endpoint."""

from fastapi.testclient import TestClient

from practice_llm.api.main import app


def test_health_reports_ready() -> None:
    """The health endpoint should expose the stable readiness contract."""
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
