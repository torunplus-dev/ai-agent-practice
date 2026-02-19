from fastapi.testclient import TestClient

from hotel_agent.main import app

client = TestClient(app)


def test_editor_has_center_table() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "編集用ペイン" in response.text
    assert "<table" in response.text
    assert "ログ / レコード / 設定一覧" in response.text
