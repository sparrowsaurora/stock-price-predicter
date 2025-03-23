import tkinter as tk
from functions import Functions
# Create an instance of Functions
functions = Functions()

# Create the main window
root = tk.Tk()

# Define ticker before using it
ticker = "AAPL"

root.title(f"Stock > {ticker.upper()}")
root.geometry("600x350")  # Set the window size X:Y

# Add a label
label = tk.Label(root, text=f"{ticker.upper()}", font=("Arial", 16))
label.pack(pady=20, anchor="nw")


button = tk.Button(root, text="Change Ticker", command=lambda: functions.next_ticker(label))
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
