
from tkinter import *
from tkinter import ttk
root = Tk()
home = ttk.Frame(root, padding=10)
home.grid()
ttk.Label(home, text="Welcome to the banking app").grid(column=0, row=0)
ttk.Button(home, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()