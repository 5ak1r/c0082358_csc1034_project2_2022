from tkinter import *
from tkinter import ttk
from client import *

new_data = []


# No docstrings for main since it is all just GUI stuff. Not really relevant to the client functions.

def eCollect(e):
    v = e.get()
    e.delete(0, END)
    return v


def efCollect(ef):
    vf = ef.get()
    ef.delete(0, END)
    try:
        return float(vf)
    except ValueError:
        return vf


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


def grid(e1, e2, e3, e4, e5, e6, e7, e8):
    e1.grid(column=1, row=0, columnspan=2)
    e2.grid(column=1, row=1, columnspan=2)
    e3.grid(column=1, row=2, columnspan=2)
    e4.grid(column=1, row=3, columnspan=2)
    e5.grid(column=1, row=4, columnspan=2)
    e6.grid(column=1, row=5, columnspan=2)
    e7.grid(column=1, row=6, columnspan=2)
    e8.grid(column=1, row=7, columnspan=2)


def add(root):
    root.destroy()
    root, home = createRoot("Add", True)
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

    grid(e1, e2, e3, e4, e5, e6, e7, e8)

    def collectAndAdd():
        current_client = Client(eCollect(e1), eCollect(e2), eCollect(e3), eCollect(e4), eCollect(e5),
                                eCollect(e6), efCollect(e7), efCollect(e8))

        if not current_client.add():
            success_root, success_home = createRoot("Success!", 1)
            ttk.Label(success_home, text="Client successfully added.").grid(row=0, column=1)

            updateRoot(success_root)

    ttk.Button(home, text="Add", command=collectAndAdd).grid(column=1, row=300)

    updateRoot(root)
    return root


def collectAndEdit(e1, e2, e3, e4, e5, e6, e7, e8, current_client):
    global new_data
    new_data = [eCollect(e1), eCollect(e2), eCollect(e3), eCollect(e4), eCollect(e5), eCollect(e6),
                efCollect(e7), efCollect(e8)]
    edited_client = Client(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4], new_data[5],
                           new_data[6], new_data[7])

    editor = {current_client[0]: new_data[0],
              current_client[1]: new_data[1],
              current_client[2]: new_data[2],
              current_client[3]: new_data[3],
              current_client[4]: new_data[4],
              current_client[5]: new_data[5],
              current_client[6]: new_data[6],
              current_client[7]: new_data[7]}

    if edited_client.edit(editor):
        success_root, success_home = createRoot("Success!", 1)
        ttk.Label(success_home, text="Client successfully edited.").grid(row=0, column=1)

        updateRoot(success_root)



def beginEdview(root, current_client, edview):
    root.destroy()

    root, home = createRoot(f"{edview.title()}", True)

    ttk.Label(home, text="First Name").grid(column=0, row=0)
    ttk.Label(home, text="Last Name").grid(column=0, row=1)
    ttk.Label(home, text="Title").grid(column=0, row=2)
    ttk.Label(home, text="Preferred Pronouns").grid(column=0, row=3)
    ttk.Label(home, text="Date of Birth").grid(column=0, row=4)
    ttk.Label(home, text="Occupation").grid(column=0, row=5)
    ttk.Label(home, text="Balance").grid(column=0, row=6)
    ttk.Label(home, text="Overdraft Limit").grid(column=0, row=7)

    string1 = StringVar()
    string1.set(current_client[0])
    string2 = StringVar()
    string2.set(current_client[1])
    string3 = StringVar()
    string3.set(current_client[2])
    string4 = StringVar()
    string4.set(current_client[3])
    string5 = StringVar()
    string5.set(current_client[4])
    string6 = StringVar()
    string6.set(current_client[5])
    string7 = StringVar()
    string7.set(current_client[6])
    string8 = StringVar()
    string8.set(current_client[7])

    e1 = ttk.Entry(home, textvariable=string1)
    e2 = ttk.Entry(home, textvariable=string2)
    e3 = ttk.Entry(home, textvariable=string3)
    e4 = ttk.Entry(home, textvariable=string4)
    e5 = ttk.Entry(home, textvariable=string5)
    e6 = ttk.Entry(home, textvariable=string6)
    e7 = ttk.Entry(home, textvariable=string7)
    e8 = ttk.Entry(home, textvariable=string8)

    if edview != "edit":
        e1.config(state="readonly")
        e2.config(state="readonly")
        e3.config(state="readonly")
        e4.config(state="readonly")
        e5.config(state="readonly")
        e6.config(state="readonly")
        e7.config(state="readonly")
        e8.config(state="readonly")
    else:
        ttk.Button(home, text="Edit",
                   command=lambda: collectAndEdit(e1, e2, e3, e4, e5, e6, e7, e8, current_client)).grid(column=1,
                                                                                                        row=300)

    grid(e1, e2, e3, e4, e5, e6, e7, e8)

    updateRoot(root)
    return root


def beginSearch(root, e1, e2, e3, edview):
    e1_val = eCollect(e1)
    e2_val = eCollect(e2)
    e3_val = eCollect(e3)

    current_client = searchEdit(e1_val, e2_val, e3_val)

    if current_client is None:
        fail_root, fail_home = createRoot("Failure", 1)

        ttk.Label(fail_home, text="That Client does not exist.").grid(column=0, row=0)
        updateRoot(fail_root)

    if edview != "delete":
        beginEdview(root, current_client, edview)
    else:
        current_client = Client(current_client[0], current_client[1], current_client[2], current_client[3],
                                current_client[4], current_client[5], float(current_client[6]),
                                float(current_client[7]))

        if current_client.delete():
            success_root, success_home = createRoot("Success!", 1)
            ttk.Label(success_home, text="Client successfully deleted.").grid(row=0, column=1)

            updateRoot(success_root)

    return root


def edview(root, edview):
    root.destroy()
    root, home = createRoot(f"{edview.title()}", True)

    ttk.Label(home, text=f"Enter the Name and Date of Birth of the client you wish to {edview}: ").grid(column=0, row=0,
                                                                                                        columnspan=2)
    ttk.Label(home, text="First Name: ").grid(column=0, row=1)
    ttk.Label(home, text="Last Name: ").grid(column=0, row=2)
    ttk.Label(home, text="Date of Birth: ").grid(column=0, row=3)

    e1 = ttk.Entry(home)
    e2 = ttk.Entry(home)
    e3 = ttk.Entry(home)

    e1.grid(column=1, row=1)
    e2.grid(column=1, row=2)
    e3.grid(column=1, row=3)

    ttk.Button(home, text=f"{edview.title()}", command=lambda: beginSearch(root, e1, e2, e3, edview))\
        .grid(column=1, row=300)

    updateRoot(root)
    return root


def showView(root, e1, search):
    try:
        searcher = eCollect(e1)
        root.destroy()
    except AttributeError:
        searcher = str()

    root = Tk()
    root.title("View")

    data = searchView(search, searcher)

    scroll = Scrollbar(root, orient='vertical')
    scroll.pack(side=RIGHT, fill='y')

    text = Text(root, yscrollcommand=scroll.set)

    for j in data:
        text.insert(END, j)

    if not data:
        text.insert(END, "No clients found.")

    scroll.config(command=text.yview)

    text.pack()

    ttk.Button(root, text="Back", command=lambda: view(root)).pack(side=LEFT)
    ttk.Button(root, text="Quit", command=root.destroy).pack(side=RIGHT)
    updateRoot(root)

    return root


def multiView(root, search):
    root.destroy()

    if search[0] not in ["n", "a"]:
        root, home = createRoot("View", True)

        ttk.Label(home, text=f"Enter {search.upper()} to search for: ").grid(column=0, row=0)
        e1 = ttk.Entry(home)
        e1.grid(column=1, row=0, columnspan=2)

        ttk.Button(home, text="Search", command=lambda: showView(root, e1, search)).grid(column=1, row=300)
    else:
        showView(None, None, search)

    updateRoot(root)
    return root


def view(root):
    root.destroy()
    root, home = createRoot("View", True)

    ttk.Label(home, text="How would you like to search for the client(s) to view?").grid(column=1, row=0)
    ttk.Button(home, text="Full Name and DOB", command=lambda: edview(root, "view")).grid(column=1, row=1)
    ttk.Button(home, text="Full Name", command=lambda: multiView(root, "full name")).grid(column=1, row=2)
    ttk.Button(home, text="Date of Birth", command=lambda: multiView(root, "dob")).grid(column=1, row=3)
    ttk.Button(home, text="Negative Balance", command=lambda: multiView(root, "negative balance")).grid(column=1, row=4)
    ttk.Button(home, text="Show all clients", command=lambda: multiView(root, "all")).grid(column=1, row=5)
    updateRoot(root)
    return root


def main(root):
    root.destroy()
    root, home = createRoot("Clients", None)

    ttk.Label(home, text="Dealing with clients").grid(column=0, row=0)
    ttk.Button(home, text="Add", command=lambda: add(root)).grid(column=0, row=1)
    ttk.Label(home, text="Add a new client to the bank").grid(column=1, row=1)
    ttk.Button(home, text="Edit", command=lambda: edview(root, "edit")).grid(column=0, row=2)
    ttk.Label(home, text="Edit the details of an existing client").grid(column=1, row=2)
    ttk.Button(home, text="Delete", command=lambda: edview(root, "delete")).grid(column=0, row=3)
    ttk.Label(home, text="Delete a client and their data").grid(column=1, row=3)
    ttk.Button(home, text="View", command=lambda: view(root)).grid(column=0, row=4)
    ttk.Label(home, text="View client information").grid(column=1, row=4)

    updateRoot(root)
    return root


def start(root):
    # Going back to the starting screen should remove the currently open widget. Need to make sure there is no error on
    # initial startup (when a previous widget does not exist)
    try:
        root.destroy()
    except AttributeError:
        pass

    root, home = createRoot("Welcome", False)

    ttk.Label(home, text="Welcome to the banking app").grid(column=1, row=0)

    updateRoot(root)
    return root


start(None)
