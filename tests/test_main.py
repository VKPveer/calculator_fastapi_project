from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["version"] == "1.1.0"


def test_health_details():
    response = client.get("/health/details")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_divide_by_zero():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400


def test_power():
    response = client.post("/power", json={"a": 2, "b": 4})
    assert response.status_code == 200
    assert response.json()["result"] == 16


def test_average():
    response = client.post("/average", json={"a": 10, "b": 20})
    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_absolute_difference():
    response = client.post(
        "/absolute-difference",
        json={"a": 5, "b": 12}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 7


def test_sum_of_squares():
    response = client.post(
        "/sum-of-squares",
        json={"a": 3, "b": 4}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 25


def test_percentage():
    response = client.post(
        "/percentage",
        json={"value": 250, "percentage": 12}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 30

def test_clamp():
    response = client.post(
        "/clamp",
        json={"value": 15, "minimum": 0, "maximum": 10}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 10


def test_percentage_change():
    response = client.post(
        "/percentage-change",
        json={"old_value": 100, "new_value": 125}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 25


def test_mean():
    response = client.post("/mean", json={"values": [2, 4, 6, 8]})
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_range():
    response = client.post("/range", json={"values": [2, 7, 11, 4]})
    assert response.status_code == 200
    assert response.json()["result"] == 9

