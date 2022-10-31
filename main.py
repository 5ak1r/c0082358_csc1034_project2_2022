
from tkinter import *
from tkinter import ttk
from client import *

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


h = Client("Sakir","Azimkar","Mr","He/Him","30/06/1674","Student",300,500)