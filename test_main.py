from fastapi.testclient import TestClient
from main import app

# Initialize the FastAPI verification client mock environment
client = TestClient(app)

def test_root_welcome_note():
    """
    Validates that the Root path successfully returns the participant's customized message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Python App! Participant: Mark"}

def test_generate_checksum_endpoint():
    """
    Validates that the POST /generate path parses JSON string elements and returns correct hashes.
    """
    payload_data = {"text": "hello"}
    # Expected MD5 hash string for 'hello' is '5d41402abc4b2a76b9719d911017c592'
    expected_hash = "5d41402abc4b2a76b9719d911017c592"
    
    response = client.post("/generate", json=payload_data)
    
    assert response.status_code == 200
    assert "checksum" in response.json()
    assert response.json()["checksum"] == expected_hash
