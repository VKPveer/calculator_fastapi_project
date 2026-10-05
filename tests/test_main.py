from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_divide_by_zero():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
