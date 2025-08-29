import os
from dotenv import load_dotenv
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta

from tools.tools import Tools
from data.formatting import Formatting

load_dotenv()

class Stock:
    def __init__(self, ticker: str, shares_owned: int = 0):
        self.ticker = ticker.upper()
        self.shares_owned = shares_owned

        # Set up Alpaca client
        self.client = StockHistoricalDataClient(
            api_key=os.getenv("APCA_API_KEY_ID"),
            secret_key=os.getenv("APCA_API_SECRET_KEY")
        )

        # Get daily prices
        price_list = self.get_day_prices()
        self.prices = {
            "open": price_list[0],
            "low": price_list[1],
            "high": price_list[2],
            "close": price_list[3]
        }

        self.current_price = self.get_current_price()
        self.change_percent = self.get_change_percent()
        self.day_change_percent = self.get_day_change_percent()

    def __repr__(self) -> str:
        current_price = self.get_current_price()
        worth = current_price * self.shares_owned
        return f"Stock {{ '{self.ticker}' : ${current_price:.2f}, Shares: {self.shares_owned}, Worth: ${worth:.2f} }}"

    ################ Get Methods ######################

    def get_stock_by_ticker(self, ticker: str):
        return Stock(ticker)

    def get_signal(self) -> str:
        # TODO: hook up to prediction model
        return "HOLD"

    def get_current_price(self) -> float:
        req = StockLatestQuoteRequest(symbol_or_symbols=self.ticker)
        quote = self.client.get_stock_latest_quote(req)
        return quote[self.ticker].ask_price or quote[self.ticker].bid_price

    def get_day_prices(self) -> list:
        # Get today's OHLC
        today = datetime.now().date()
        start = today - timedelta(days=2)  # buffer in case today is a holiday/weekend
        req = StockBarsRequest(
            symbol_or_symbols=self.ticker,
            timeframe=TimeFrame.Day,
            start=start
        )
        bars = self.client.get_stock_bars(req).df
        bars = bars.loc[self.ticker]
        latest = bars.iloc[-1]
        return [latest.open, latest.low, latest.high, latest.close]

    def get_day_change_percent(self) -> float:
        prices = self.get_day_prices()
        open_price, close_price = prices[0], prices[3]
        return ((close_price - open_price) / open_price) * 100

    @Tools.timer
    def get_history(self, length: str = "1M") -> dict:
        # Convert user-friendly period to timedelta
        mapping = {
            "1D": timedelta(days=1),
            "5D": timedelta(days=5),
            "1M": timedelta(days=30),
            "3M": timedelta(days=90),
            "6M": timedelta(days=180),
            "1Y": timedelta(days=365)
        }
        delta = mapping.get(length, timedelta(days=30))
        start = datetime.now() - delta

        req = StockBarsRequest(
            symbol_or_symbols=self.ticker,
            timeframe=TimeFrame.Day,
            start=start
        )
        bars = self.client.get_stock_bars(req).df
        bars = bars.loc[self.ticker]

        # Convert to dictionary {date: closing price}
        return {str(date.date()): round(price, 2) for date, price in zip(bars.index, bars["close"])}

    @Tools.timer
    def get_change_percent(self) -> float:
        # Compare current price with last close
        prices = self.get_day_prices()
        last_close = prices[3]
        current = self.get_current_price()
        return ((current - last_close) / last_close) * 100

    ################ PROPERTIES ######################

    @property
    def display_formatted(self):
        """Formats and prints the stock data."""
        cont = self.rawdata
        return Formatting.stock_base(cont[0], cont[1])

    @property
    def signal(self) -> str:
        return self.get_signal()

    @property
    def rawdata(self) -> list:
        current_price = self.get_current_price()
        change_percent = self.get_change_percent()
        return [self.ticker, current_price, self.shares_owned, change_percent]
