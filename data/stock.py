class Stock:
    def __init__(self, ticker:str, shares_owned:int = 0, invested:float = 0):   
        self.ticker = ticker
        self.shares_owned = shares_owned
        self.invested = invested
    
    def __str__(self) -> str:
        current_price = self.get_current_price()
        worth = current_price * self.shares_owned
        return f"{self.ticker} -- curr: {current_price}\nOwned: {self.shares_owned} -- Worth: {worth}"

    def get_current_price(self):
        current_price:float = 10.40 #temporary value
        return current_price

