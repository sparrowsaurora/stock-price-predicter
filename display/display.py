import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from display.functions import Functions
from display.graph import Graph

class Display:
    def __init__(self):
        pass

    @staticmethod
    def main():
        # Create an instance of Functions
        functions = Functions()

        # Create the main window
        root = tk.Tk()

        # Define ticker before using it
        ticker = "AAPL"

        root.title(f"Stock > {ticker.upper()}")
        root.geometry("800x600")  # Adjusted window size to fit the graph

        # Add a label
        label = tk.Label(root, text=ticker.upper(), font=("Arial", 16))
        label.pack(pady=20, anchor="nw")

        # Update both label and window title
        button = tk.Button(root, text="Change Ticker", command=lambda: functions.next_ticker(label, root))
        button.pack(pady=10, anchor="nw")

        # Create the graph
        Graph.create_graph()  # Create an empty graph

        # Plot the data onto the graph
        Graph.plot_graph()  # Plot the stock data

        # Create a canvas to display the graph inside Tkinter
        canvas = FigureCanvasTkAgg(Graph.fig, master=root)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Start the Tkinter event loop
        root.mainloop()