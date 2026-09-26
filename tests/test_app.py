from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.delete("/activities/Chess%20Club/unregister?email=michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"
    assert "michael@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_participant_returns_404_for_missing_activity():
    response = client.delete("/activities/Unknown%20Club/unregister?email=test@example.com")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
