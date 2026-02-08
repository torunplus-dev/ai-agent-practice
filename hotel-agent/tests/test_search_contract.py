from fastapi.testclient import TestClient

from hotel_agent.main import app


def test_search_contract() -> None:
    client = TestClient(app)
    payload = {"prompt": "東京で3泊、駅近のホテル"}
    response = client.post("/search", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == {
        "query",
        "results",
        "questions",
        "explanation",
        "meta",
    }
    assert isinstance(data["results"], list)
    assert isinstance(data["questions"], list)
    assert isinstance(data["meta"], dict)
