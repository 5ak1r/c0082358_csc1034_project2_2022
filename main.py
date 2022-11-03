
from tkinter import *
from tkinter import ttk
from client import *


def add():
    None

def edit():
    None

def delete():
    None

def view():
    None

def main(root):
    root.destroy()
    root = Tk()
    root.title("Clients")


    home = ttk.Frame(root, padding=10)
    home.grid()
    ttk.Label(home, text="Dealing with clients").grid(column=0,row=0)
    ttk.Button(home, text="Add", command=add).grid(column=0, row=1)
    ttk.Label(home, text="Add a new client to the bank").grid(column=1,row=1)
    ttk.Button(home, text="Edit", command=edit).grid(column=0, row=2)
    ttk.Label(home, text="Edit the details of an existing client").grid(column=1,row=2)
    ttk.Button(home, text="Delete", command=view).grid(column=0, row=3)
    ttk.Label(home, text="Delete a client and their data").grid(column=1, row=3)
    ttk.Button(home, text="View", command=view).grid(column=0, row=4)
    ttk.Label(home, text="View client information").grid(column=1, row=4)

    root.update()
    root.geometry("+{}+{}".format(int((root.winfo_screenwidth()-root.winfo_width())/2),
                                  int((root.winfo_screenheight()-root.winfo_height())/2)))
    root.mainloop()
def start():
    root = Tk()
    root.title("Welcome")
    home = ttk.Frame(root, padding=10)
    home.grid()
    ttk.Label(home, text="Welcome to the banking app").grid(column=1, row=0)
    ttk.Button(home, text="Quit", command=root.destroy).grid(column=2, row=1)
    ttk.Button(home, text="Start", command=lambda: main(root)).grid(column=0,row=1)
    root.update()
    root.geometry("+{}+{}".format(int((root.winfo_screenwidth()-root.winfo_width())/2),
                                  int((root.winfo_screenheight()-root.winfo_height())/2)))
    root.mainloop()
    return root

#h = Client("Sakir","Azimkar","Mr","He/Him","30/06/1674","Student",300,500)

start()