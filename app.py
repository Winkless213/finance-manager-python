import tkinter as tk
from database import init_db
from gui import FinanceApp

if __name__ == "__main__":
    init_db()

    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()