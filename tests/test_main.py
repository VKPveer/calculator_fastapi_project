from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["version"] == "1.5.0"


def test_health_details():
    response = client.get("/health/details")
    assert response.status_code == 200
    assert "finance" in response.json()["capabilities"]


def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_divide_by_zero():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400


def test_clamp():
    response = client.post(
        "/clamp",
        json={"value": 15, "minimum": 0, "maximum": 10},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 10


def test_percentage_change():
    response = client.post(
        "/percentage-change",
        json={"old_value": 100, "new_value": 125},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 25


def test_median():
    response = client.post("/median", json={"values": [7, 1, 3, 5]})
    assert response.status_code == 200
    assert response.json()["result"] == 4


def test_weighted_average():
    response = client.post(
        "/weighted-average",
        json={"values": [10, 20, 30], "weights": [1, 2, 1]},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 20


def test_normalize():
    response = client.post(
        "/normalize",
        json={"value": 50, "minimum": 0, "maximum": 100},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 0.5


def test_ratio():
    response = client.post("/ratio", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json()["result"] == 2.5


def test_compound_amount():
    response = client.post(
        "/compound-amount",
        json={
            "principal": 1000,
            "annual_rate_percent": 10,
            "years": 2,
            "compounds_per_year": 1,
        },
    )
    assert response.status_code == 200
    assert response.json()["result"] == 1210


def test_celsius_to_fahrenheit():
    response = client.post(
        "/celsius-to-fahrenheit",
        json={"value": 0},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 32


def test_fahrenheit_to_celsius():
    response = client.post(
        "/fahrenheit-to-celsius",
        json={"value": 212},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 100


def test_kilometers_to_miles():
    response = client.post(
        "/kilometers-to-miles",
        json={"value": 10},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 6.2137


def test_tax_amount():
    response = client.post(
        "/tax-amount",
        json={"amount": 200, "tax_percent": 10},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 20


def test_total_with_tax():
    response = client.post(
        "/total-with-tax",
        json={"amount": 200, "tax_percent": 10},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 220
