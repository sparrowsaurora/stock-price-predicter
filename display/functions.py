class Functions:
    def __init__(self):
        self.tickers = ['AAPL', 'NVDA', 'AMZN', 'GOOGL', 'META', 'ADBE']
        self.index = 0  # Track current ticker
        

    def next_ticker(self, label):
        """Update the label with the next ticker."""
        self.index = (self.index + 1) % len(self.tickers)  # Loop through tickers
        label.config(text=self.tickers[self.index])  # Update label text
