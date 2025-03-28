class Functions:
    def __init__(self):
        self.tickers = ['AAPL', 'NVDA', 'AMZN', 'GOOGL', 'META', 'ADBE']
        self.index = 0  # Track current ticker
        self.ticker = self.tickers[0]

    def get_ticker(self):
        return self.ticker

    def next_ticker(self) -> None:
        """Update the label and window title with the next ticker."""
        self.index = (self.index + 1) % len(self.tickers)  # Loop through tickers
        self.ticker = self.tickers[self.index]
        
    def update_label(self, label, root):
        label.config(text=self.ticker)  # Update label text
        root.title(f"Stock > {self.ticker}")  # Update window title
    
    def next_update_ticker(self, label, root):
        self.next_ticker()
        self.update_label(label, root)
        return self.ticker

        
