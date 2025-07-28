# Run with: uvicorn display/api:app --reload




from fastapi import FastAPI
app = FastAPI()

# GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/{ticker}/")
def get_stock(ticker: str):
    return {"ticker": ticker.upper(), "message": f"Fetching data for {ticker.upper()}"}

@app.get("/{ticker}/pretty/")
def get_stock(ticker: str):
    
    return 



