from termcolor import colored
from tabulate import tabulate

class Formatting:   
    @staticmethod
    def single(data) -> str:
        # a static method; returns a single formatted piece of data 
        # Ensure text is a string
        data = str(data)
        top = f"+{'─' * len(data)}+"
        middle = f"│{data:^8}│"
        bottom = f"+{'─' * len(data)}+"
        return f"{top}\n{middle}\n{bottom}"
    
    @staticmethod
    def stock_base(ticker: str, price: float) -> str:
        data = [[ticker, f"{price:.2f}"]]
        return tabulate(data, tablefmt="grid")
    
    @staticmethod
    def basic_stats(self, ticker: str, current_price: float | int, shares_owned: int, change_percent: str) -> str:
        # a static method; returns all the basic information in a formatted way
        # Uses
        #   Formatting._percent_styleing to color "change-percent param"
        # Params:
        #   self..
        #   Ticker - name of the stock: Str
        #   Current_price - current stock's price: Float
        #   Shares_owned - no. of shares owned: Int
        #   change_percent - the percent of change in the stock. 24h: Float
        headers = ["Ticker", "Price", "Shares", "Change %"]

        change_percent = self._percent_styling(change_percent)
        current_price = float(current_price)
        data = [
            [ticker.upper(), f"{current_price:.2f}", f"{shares_owned:,}", change_percent]
        ]
        return tabulate(data, headers=headers, tablefmt="grid")
    
    def _percent_styling(change_percent: int | float) -> str:
        # returns a coloured and signed version of change_percent
        if change_percent == 0:
            return colored(f"/ {change_percent}", "dark_grey")
        return colored("+" + str(change_percent), "green") if change_percent >= 0 else colored("-" + str(change_percent), "red")
    
    @staticmethod
    def print_history(data: dict) -> str:
        table = [[date, f"{price:.2f}"] for date, price in data.items()]
        headers = ["Date", "Price"]
        print(tabulate(table, headers=headers, tablefmt="orgtbl"))
            