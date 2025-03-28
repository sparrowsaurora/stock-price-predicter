from data.stock import Stock
from data.formating import Formatting
from display.display import Display

display = Display()
display.main()
# print(Formatting.basic_stats("APL", 10.63, 500, 1.08))

# stock = Stock("aapl")

# Formatting.print_history(stock.history('1mo'))

# stock = yf.Ticker("AAPL")  # Replace "AAPL" with any stock ticker symbol
# info = stock.history(period="1mo")  # Fetch general info about the stock
# print(info)

# current_price = stock.history(period="1d")["Close"].iloc[-1]
# print(f"Current price: ${current_price:.2f}")

# recommendations = stock.recommendations
# print(recommendations)
