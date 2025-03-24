from termcolor import colored

class Formatting:
    def __init__(self):
        pass
    
    @staticmethod
    def single(data) -> str:
        # a static method; returns a single formatted piece of data 
        return f"-----------\n| {data:^8} |\n-----------"
    
    @staticmethod
    def basic_stats(self, ticker, current_price, shares_owned, change_percent) -> str:
        # a static method; returns all the basic information in a formatted way
        # Uses
        #   Formatting.percent_styleing to color "change-percent param"
        # Params:
        #   self..
        #   Ticker - name of the stock: Str
        #   Current_price - current stock's price: Float
        #   Shares_owned - no. of shares owned: Int
        #   change_percent - the percent of change in the stock. 24h: Float
        change_percent = self.percent_styling(change_percent)
        return f"----------------------------\n| {ticker.upper()} | {current_price:.2f} | {shares_owned:,} | {change_percent} |\n----------------------------"
    
    def percent_styling(change_percent) -> str:
        # returns a coloured and signed version of change_percent
        return colored("+" + str(change_percent), "green") if change_percent >= 0 else colored("-" + str(change_percent), "red")
