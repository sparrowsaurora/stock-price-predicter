import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from display.functions import Functions
from display.graph import Graph

class Display:
    def __init__(self):
        self.functions = Functions()
        self.ticker = self.functions.get_ticker()

    def main(self):
        # Create an instance of Functions
        

        # Create the main window
        root = tk.Tk()

        # Define ticker before using it
        

        root.title(f"Stock > {self.ticker.upper()}")
        root.geometry("800x600")  # Adjusted window size to fit the graph

        # Add a label
        label = tk.Label(root, text=self.ticker.upper(), font=("Arial", 16))
        label.pack(pady=20, anchor="nw")

        def update_ticker(label, root):
            self.ticker = self.functions.next_update_ticker(label, root)
            Graph.clear()
            Graph.plot_graph(self.ticker)
            print("at update_ticker")

        # Update both label and window title
        button = tk.Button(root, text="Change Ticker", command=lambda: update_ticker(label, root))
        button.pack(pady=10, anchor="nw")

        Graph.create_graph()  # Create an empty graph
        print("at create_graph")

        Graph.plot_graph(self.ticker)  # Plot the stock data

        # Create a canvas to display the graph inside Tkinter
        canvas = FigureCanvasTkAgg(Graph.fig, master=root)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Start the Tkinter event loop
        root.mainloop()