import matplotlib.pyplot as plt
from data.stock import Stock

class Graph:
    @staticmethod
    def create_graph():
        print("creating graph")
        """Creates an empty graph."""
        Graph.fig, Graph.ax = plt.subplots()  # Create figure and axis
        Graph.ax.set_xlabel("Date")
        Graph.ax.set_ylabel("Price (USD)")
        return Graph.fig
    
    @staticmethod
    def plot_graph(ticker):
        """Plots stock data onto the existing graph."""
        print("plotting graph")
        print("this step takes a fucting while from the api call")
        length = '1mo'
        stock = Stock(ticker)
        data = stock.history(length)
        plt.plot(data.keys(), data.values(), label=f"{ticker} Stock Price")
        plt.title(f"{ticker} Stock Price Over Past {length}")
        plt.legend()

        # data = {
        #     1: 10.64, 2: 10.75, 3: 10.92, 4: 10.80, 5: 10.95,
        #     6: 11.10, 7: 11.05, 8: 11.23, 9: 11.35, 10: 11.50,
        #     11: 11.30, 12: 11.45, 13: 11.60, 14: 11.75, 15: 11.90,
        #     16: 12.10, 17: 12.05, 18: 12.30, 19: 12.50, 20: 12.70,
        #     21: 12.40, 22: 12.55, 23: 12.80, 24: 12.95, 25: 13.10,
        #     26: 13.25, 27: 13.50, 28: 13.75, 29: 13.95, 30: 14.10
        # }

        # # Extract dates and prices using a simple for loop
        # dates = []
        # prices = []
        # for date, price in data.items():
        #     dates.append(date)
        #     prices.append(price)
        
        # Graph.ax.plot(dates, prices, marker="o", linestyle="--", label="Stock A")
        # # Graph.ax.legend()  # Add legend
        # plt.draw()  # Redraw the updated graph
        # plt.pause(0.1)  # Pause to allow UI update

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def clear():
        Graph.fig.clear()
        print("at clear function")

