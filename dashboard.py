# dashboard.py
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class Dashboard(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Dashboard")
        self.geometry("1100x650")
        
        # Example content
        label = tb.Label(self, text="Welcome to the Dashboard", font=("Helvetica", 20))
        label.pack(pady=50)

        # Example summary cards or placeholders
        tb.Label(self, text="Total Invoices: 0", bootstyle="info").pack(pady=10)
        tb.Label(self, text="Total Revenue: $0.00", bootstyle="success").pack(pady=10)
