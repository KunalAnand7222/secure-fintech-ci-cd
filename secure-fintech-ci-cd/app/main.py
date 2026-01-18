from fastapi import FastAPI
app=FastAPI()
@app.get("/health")
def h():
    return {"status":"ok"}
@app.get("/stocks")
def s():
    return [{"symbol":"AAPL","price":189.3},{"symbol":"GOOGL","price":141.7}]
