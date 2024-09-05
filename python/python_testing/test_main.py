from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_repeat_text_valid():
    response = client.get("/repeat_text?text=hello&times=3")
    assert response.status_code == 200
    assert response.json() == "hellohellohello"


def test_repeat_text_invalid():
    response = client.get("/repeat_text?text=hello&times=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "The 'times' parameter must be less than 5."}
