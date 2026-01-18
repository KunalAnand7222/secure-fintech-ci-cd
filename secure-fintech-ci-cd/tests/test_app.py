from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_health():
    assert c.get("/health").status_code==200
def test_stocks():
    r=c.get("/stocks")
    assert r.status_code==200
    assert isinstance(r.json(),list)
