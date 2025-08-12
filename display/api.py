# Run with: uvicorn display.api:app --reload

from data.stock import Stock



from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="display/pages/static"), name="static")

htmlpage_route = "display/pages/"

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def read_root():
    # make a graph image and project summary root page?
    with open(htmlpage_route+"index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/about", response_class=HTMLResponse, include_in_schema=False)
def read_root():
    # make a graph image and project summary root page?
    with open(htmlpage_route+"about.html", "r", encoding="utf-8") as f:
        return f.read()

# GET Endpoints
@app.get("/{ticker}/")
def get_stock(ticker: str):
    stock = Stock.get_stock_by_ticker(ticker)
    # returns graph data and signal
    response = {"signal":"stock.signal"}
    return response

@app.get("/{ticker}/raw/")
def get_stock_raw(ticker: str):
    # stock's data in raw format
    stock = Stock.get_stock_by_ticker(ticker)
    response = {
        "ticker": stock.ticker,
        "shares": stock.shares_owned,
        "current_price": stock.current_price,
        "signal": "stock.signal"
        }
    return response

@app.get("/{ticker}/pretty/")
def get_stock_pretty(ticker: str):
    stock = Stock.get_stock_by_ticker(ticker)
    return stock.display_formatted

# POST Endpoints

@app.post('/{account}/add/')
def add_stock_to_portfolio(account: str, ticker: str, quantity: int):
    raise NotImplementedError
    return {"message":f"{ticker} Added.", "quantity": f"{quantity}"}

@app.post('/{account}/rem/')
def rem_stock_from_portfolio(account: str, ticker: str, quantity: int):
    raise NotImplementedError
    return {"message":f"{ticker} Removed.", "quantity": f"{quantity}"}
