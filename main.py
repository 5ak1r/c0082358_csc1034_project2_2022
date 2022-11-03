from tkinter import *
from tkinter import ttk
from client import *


def createRoot(title, back):
    root = Tk()
    root.title(title)

    home = ttk.Frame(root, padding=10)
    home.grid()
    try:
        if back == True:
            ttk.Button(home, text="Back", command=lambda: main(root)).grid(column=0, row=300)
        else:
            ttk.Button(home, text="Start", command=lambda: main(root)).grid(column=0, row=1)
    except TypeError:
        ttk.Button(home, text="Back", command=lambda: start(root)).grid(column=0, row=300)
    return root, home


def updateRoot(root):
    root.update()
    root.geometry("+{}+{}".format(int((root.winfo_screenwidth() - root.winfo_width()) / 2),
                                  int((root.winfo_screenheight() - root.winfo_height()) / 2)))
    root.mainloop()
    return root


def add(root):
    root.destroy()
    root, home = createRoot("Add", True)

    updateRoot(root)
    return root


def edit(root):
    root.destroy()
    root, home = createRoot("Edit", True)

    updateRoot(root)
    return root


def delete(root):
    root.destroy()
    root, home = createRoot("Delete", True)

    updateRoot(root)
    return root


def view(root):
    root.destroy()
    root, home = createRoot("View", True)

    updateRoot(root)
    return root


def main(root):
    root.destroy()
    root, home = createRoot("Clients", "main")

    ttk.Label(home, text="Dealing with clients").grid(column=0, row=0)
    ttk.Button(home, text="Add", command=lambda: add(root)).grid(column=0, row=1)
    ttk.Label(home, text="Add a new client to the bank").grid(column=1, row=1)
    ttk.Button(home, text="Edit", command=lambda: edit(root)).grid(column=0, row=2)
    ttk.Label(home, text="Edit the details of an existing client").grid(column=1, row=2)
    ttk.Button(home, text="Delete", command=lambda: delete(root)).grid(column=0, row=3)
    ttk.Label(home, text="Delete a client and their data").grid(column=1, row=3)
    ttk.Button(home, text="View", command=lambda: view(root)).grid(column=0, row=4)
    ttk.Label(home, text="View client information").grid(column=1, row=4)

    updateRoot(root)
    return root


def start(root):
    # Going back to the starting screen should remove the currently open widget. Need to make sure there is no error on
    # initial startup (when a previous widget does not exist)
    """
    Starting screen; main navigation to all the application's functionality
    :param root: Tkinter Widget
    :return: the same widget to be destroyed upon changing screens
    """
    try:
        root.destroy()
    except AttributeError:
        None

    root, home = createRoot("Welcome", False)

    ttk.Label(home, text="Welcome to the banking app").grid(column=1, row=0)
    ttk.Button(home, text="Quit", command=root.destroy).grid(column=2, row=1)

    updateRoot(root)

    return root


# h = Client("Sakir","Azimkar","Mr","He/Him","30/06/1674","Student",300,500)
start(None)
