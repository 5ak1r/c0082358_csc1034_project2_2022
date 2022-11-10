from tkinter import *
from tkinter import ttk
from client import *


def createRoot(title, back):
    root = Tk()
    root.title(title)

    home = ttk.Frame(root, padding=10)
    home.grid()
    if isinstance(back, bool):
        if back:
            ttk.Button(home, text="Back", command=lambda: main(root)).grid(column=0, row=300)
        else:
            ttk.Button(home, text="Start", command=lambda: main(root)).grid(column=0, row=300)
    elif isinstance(back, int):
        pass
    else:
        ttk.Button(home, text="Back", command=lambda: start(root)).grid(column=0, row=300)

    if type(back) == int:
        ttk.Button(home, text="Confirm", command=root.destroy).grid(column=1, row=300)
    else:
        ttk.Button(home, text="Quit", command=root.destroy).grid(column=2, row=300)

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

    ttk.Label(home, text="First Name").grid(column=0, row=0)
    ttk.Label(home, text="Last Name").grid(column=0, row=1)
    ttk.Label(home, text="Title").grid(column=0, row=2)
    ttk.Label(home, text="Preferred Pronouns").grid(column=0, row=3)
    ttk.Label(home, text="Date of Birth").grid(column=0, row=4)
    ttk.Label(home, text="Occupation").grid(column=0, row=5)
    ttk.Label(home, text="Balance").grid(column=0, row=6)
    ttk.Label(home, text="Overdraft Limit").grid(column=0, row=7)

    e1 = ttk.Entry(home)
    e2 = ttk.Entry(home)
    e3 = ttk.Entry(home)
    e4 = ttk.Entry(home)
    e5 = ttk.Entry(home)
    e6 = ttk.Entry(home)
    e7 = ttk.Entry(home)
    e8 = ttk.Entry(home)

    e1.grid(column=1, row=0, columnspan=2)
    e2.grid(column=1, row=1, columnspan=2)
    e3.grid(column=1, row=2, columnspan=2)
    e4.grid(column=1, row=3, columnspan=2)
    e5.grid(column=1, row=4, columnspan=2)
    e6.grid(column=1, row=5, columnspan=2)
    e7.grid(column=1, row=6, columnspan=2)
    e8.grid(column=1, row=7, columnspan=2)

    def e1Collect():
        v1 = e1.get()
        e1.delete(0, END)
        return v1

    def e2Collect():
        v2 = e2.get()
        e2.delete(0, END)
        return v2

    def e3Collect():
        v3 = e3.get()
        e3.delete(0, END)
        return v3

    def e4Collect():
        v4 = e4.get()
        e4.delete(0, END)
        return v4

    def e5Collect():
        v5 = e5.get()
        e5.delete(0, END)
        return v5

    def e6Collect():
        v6 = e6.get()
        e6.delete(0, END)
        return v6

    def e7Collect():
        v7 = e7.get()
        e7.delete(0, END)
        try:
            return float(v7)
        except ValueError:
            return v7

    def e8Collect():
        v8 = e8.get()
        e8.delete(0, END)
        try:
            return float(v8)
        except ValueError:
            return v8

    def collectAndAdd():
        Client(e1Collect(), e2Collect(), e3Collect(), e4Collect(), e5Collect(), e6Collect(), e7Collect(), e8Collect())

        success_root, success_home = createRoot("Success!", 1)

        ttk.Label(success_home, text="Client successfully added.").grid(row=0, column=1)

        updateRoot(success_root)

    ttk.Button(home, text="Add", command=collectAndAdd).grid(column=1, row=300)

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
    root, home = createRoot("Clients", None)

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
        pass

    root, home = createRoot("Welcome", False)

    ttk.Label(home, text="Welcome to the banking app").grid(column=1, row=0)

    updateRoot(root)

    return root


# h = Client("Sakir","Azimkar","Mr","He/Him","30/06/1674","Student",300,500) raises an error as expected
start(None)
