class Functions:
    def __init__(self):
        self.tickers = ['AAPL', 'NVDA', 'AMZN', 'GOOGL', 'META', 'ADBE']
        self.index = 0  # Track current ticker

    def next_ticker(self, label, root) -> None:
        """Update the label and window title with the next ticker."""
        self.index = (self.index + 1) % len(self.tickers)  # Loop through tickers
        new_ticker = self.tickers[self.index]

        label.config(text=new_ticker)  # Update label text
        root.title(f"Stock > {new_ticker}")  # Update window title
