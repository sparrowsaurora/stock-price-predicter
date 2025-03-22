from termcolor import colored

class Formatting:

    def __init__(self):
        pass
    
    @staticmethod
    def single(data):
        return f"-----------\n| {float(data):^8.2f} |\n-----------"
    
    @staticmethod
    def basic_stats(ticker, current_price, shares_owned, change_percent):
        change_percent = colored("+" + str(change_percent), "green") if change_percent >= 0 else colored("-" + str(change_percent), "red")
        return f"----------------------------\n| {ticker.upper()} | {current_price:.2f} | {shares_owned:,} | {change_percent} |\n----------------------------"
    
    # f"Ticker: {self.ticker} -- Curr: {current_price}\nOwned: {self.shares_owned} -- Worth: {worth}"
    