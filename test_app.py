from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["application"] == "Parking Reservation System"
    assert data["status"] == "running"

def test_slots():
    client = app.test_client()
    response = client.get("/slots")
    assert response.status_code == 200
    data = response.get_json()
    assert data["total_slots"] == 15
    assert data["reserved_slots"] == 5
    assert data["available_slots"] == 10