import tkinter as tk
from ttkbootstrap import Style
from dashboard import Dashboard
from credits import Credits  # import your Credits class

root = tk.Tk()
style = Style(theme="darkly")
root.title("InvoiceHub")
root.geometry("1100x650")

# Functions to open windows
def open_dashboard():
    dash = Dashboard(root)
    dash.grab_set()  # optional: makes the dashboard modal

def open_credits():
    credits_window = Credits(root)
    credits_window.grab_set()  # optional: modal

# Buttons
button1 = tk.Button(root, text="Invoice", command=open_dashboard)
button1.pack(pady=20)

button2 = tk.Button(root, text="Credits", command=open_credits)
button2.pack(pady=20)

root.mainloop()
