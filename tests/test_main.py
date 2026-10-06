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

# =========================================================
# Manifest-driven endpoint tests
# =========================================================

def test_sum_of_squares_endpoint():
    response = client.post("/sum-of-squares", json={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json()["result"] == 25

def test_absolute_difference_endpoint():
    response = client.post("/absolute-difference", json={"a": 5, "b": 12})
    assert response.status_code == 200
    assert response.json()["result"] == 7

def test_is_equal_endpoint():
    response = client.post("/is-equal", json={"a": 10, "b": 10})
    assert response.status_code == 200
    assert response.json()["result"] is True

def test_greater_number_endpoint():
    response = client.post("/greater-number", json={"a": 9, "b": 4})
    assert response.status_code == 200
    assert response.json()["result"] == 9
