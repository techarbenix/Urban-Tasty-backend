from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_endpoints():
    endpoints = [
        "/",
        "/api/dashboard",
        "/api/staff",
        "/api/inventory",
        "/api/certifications",
        "/api/orders",
        "/api/delivery",
        "/api/products"
    ]
    
    for ep in endpoints:
        response = client.get(ep)
        if response.status_code == 200:
            print(f"OK: {ep}")
        else:
            print(f"FAIL: {ep} - Status: {response.status_code}")

if __name__ == "__main__":
    test_endpoints()
