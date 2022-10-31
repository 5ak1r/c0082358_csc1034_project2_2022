
from tkinter import *
from tkinter import ttk
import client

def main():
    None

def start():
    root = Tk()
    root.title("Welcome")
    home = ttk.Frame(root, padding=10)
    home.grid()
    ttk.Label(home, text="Welcome to the banking app").grid(column=1, row=0)
    ttk.Button(home, text="Quit", command=root.destroy).grid(column=2, row=1)
    ttk.Button(home, text="Start", command=main).grid(column=0,row=1)
    root.mainloop()