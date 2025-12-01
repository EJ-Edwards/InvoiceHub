import ttkbootstrap as tb
from ttkbootstrap.constants import *

class Credits(tb.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Credits")
        self.geometry("1100x650")
        
        # Example content
        label = tb.Label(self, text="Welcome to the Credits", font=("Helvetica", 20))
        label.pack(pady=50)

        credits_info = tb.Label(self, text="Developeed by EJ (Eric Edwards)", font=("Helvetica", 14))
        
        credits_info.pack(pady=20)