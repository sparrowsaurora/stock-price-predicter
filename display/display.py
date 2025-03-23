import tkinter as tk
from functions import Functions
# Create the main window
root = tk.Tk()
ticker = "aapl"
root.title(f"Stock > {ticker.upper()}")
root.geometry("600x350")  # Set the window size X:Y

# Add a label
label = tk.Label(root, text=f"{ticker.upper()}", font=("Arial", 16))
label.pack(pady=20, anchor="nw")

# Add a button
def on_button_click():
    label.config(text="{}")

button = tk.Button(root, text="Change Ticker", command=on_button_click)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
