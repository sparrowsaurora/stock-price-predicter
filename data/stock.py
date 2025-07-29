# import yfinance as yf
from tools.tools import Tools
from data.formatting import Formatting

'''REFOMAT TO USE ALPACA.MARKETS TRADING API'''

# https://yfinance-python.org/reference/yfinance.stock.html

class Stock:
    def __init__(self, ticker:str, shares_owned:int = 0, invested:float = 0):
        # To make the stock item, which will be used to make the whole project work.

        # Params:
        #     - Ticker: the stock's ticker symbol - string
        #     - Shares_owned: The number of shares the user owns in the stock - int
        #     - invested: The ammount of money initially invested - float
        self.ticker = ticker.upper()
        self.shares_owned = shares_owned
        self.invested = invested
    
    def __repr__(self) -> None:
         # Params:
        #     - self: gets basic data already related to the stock -> [str, int, float]
        # Functions:
        #     - current_price: gets current price with an api -> float
        current_price = self.get_current_price()
        worth = current_price * self.shares_owned
        return f"{self.ticker}" + "{" + f"Curr: {current_price}\nOwned: {self.shares_owned}, Worth: {worth}" + "}"
    
    # ===========================================================================================================

    def get_stock_by_ticker(ticker: str):
        # -> Stock
        
        
        return ...


    def rawdata(self) -> list[str, float, int, float]:
        #returns a list of all data in a raw format
        current_price = self.get_current_price()
        change_percent = self.get_change_percent()
        return [self.ticker, current_price, self.shares_owned, change_percent]
    # [ticker.upper(), f"{current_price:.2f}", f"{shares_owned:,}", change_percent]

    # ===========================================================================================================

    def get_current_price(self) -> float:
        # Gets the Current Price of a stock via API request
        current_price: float = 10.4 # temporary value ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        return current_price
    
    @Tools.timer
    def get_history(self, length) -> dict:
        raise NotImplementedError("we havent gotten this data from the api")
    
        # prep data to call api
        stock = yf.Ticker(self.ticker)
        length = str(length)
        history = stock.history(period=length)

        # Convert to dictionary {date: closing price}
        data = {}
        for date, price in zip(history.index, history["Close"]):
            date = str(date.date())[5:]
            value = round(price, 2)
            data[date] = value
        return data

    @Tools.timer
    def get_change_percent(self) -> float:
        raise NotImplementedError("we havent gotten this data from the api")
        return change_percent
        
    def get_signal() -> str:
        raise NotImplementedError
    
    ################ PROPERTIES ######################

    @property
    def display_formatted(self):
        """Formats and prints the stock data."""
        cont = self.rawdata()
        return Formatting.stock_base(cont[0], cont[1])
    
    @property
    def ticker(self) -> str:
        return self.ticker.upper()
    
    @property
    def shares_owned(self) -> str:
        return self.shares_owned

    @property
    def current_price(self) -> str:
        return self.get_current_price()

    @property
    def signal(self) -> str:
        return self.get_signal()


        