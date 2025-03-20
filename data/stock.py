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
    
    def __str__(self) -> str:
        # Converts the stock item with the data to a String item.

        # Params:
        #     - self: gets basic data already related to the stock - [str, int, float]
        # Functions:
        #     - current_price: gets current price with an api - float

        current_price = self.get_current_price()
        worth = current_price * self.shares_owned
        return f"Ticker: {self.ticker} -- Curr: {current_price}\nOwned: {self.shares_owned} -- Worth: {worth}"

    def get_current_price(self) -> float:
        # Gets the Current Price of a stock via API request
        current_price:float = 10.40 #temporary value
        return current_price

apl = Stock("apl", 10, 500)
print(apl.__str__())

