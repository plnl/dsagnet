from fastapi.testclient import TestClient

from dsagent.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_query_endpoint():
    response = client.post("/query", json={"prompt": "你好"})
    assert response.status_code == 200
    data = response.json()
    assert data["prompt"] == "你好"
    assert "已收到请求" in data["response"]
