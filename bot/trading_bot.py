class TradingBot:
    def __init__(self):
        self.portfolio: dict = {}

    def buy(self, ticker: str, quantity: int = 0):
        # maybe an .asm script?
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        self.portfolio[ticker] = self.portfolio.get(ticker, 0) + quantity

    def sell(self, ticker: str, quantity: int = 0):
        if ticker not in self.portfolio:
            raise KeyError("This stock is not in your portfolio.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        current_quantity = self.portfolio[ticker]
        if current_quantity < quantity:
            raise ValueError("Cannot sell more than you own.")
        self.portfolio[ticker] -= quantity
        if self.portfolio[ticker] == 0:
            del self.portfolio[ticker]
    
    def show_portfolio(self):
        print("Current Portfolio:")
        for key, value in self.portfolio.items():
            print(f"\t{key}: {value}")
        if not self.portfolio:
            print("\t(empty)")
    
    @property
    def data(self):
        return [f"{key}: {value}" for key, value in self.portfolio.items()]
