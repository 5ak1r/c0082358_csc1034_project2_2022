from datetime import datetime as dt
import os

pronouns = ["he", "him", "she", "her", "they", "them", "it", "its"]


class Client:

    # Creates a class
    def __init__(self, fname, lname, title, pp, dob, occupation, bal, overlim):
        """
        Initializing important values for each new client added to the system.

        :param fname: first name of client
        :param lname: last name of client
        :param title: title of client (Mr., Mrs., etc.)
        :param pp: Preferred Pronouns of Client
        :param dob: Date of Birth of Client
        :param occupation: Occupation of Client
        :param bal: Balance quantity of Client
        :param overlim: Overdraft Limit of Client
        """

        # Check inputs are of the correct type
        # Dates are set to be strings

        if not isinstance(fname, str):
            raise TypeError("That is not a valid first name.")

        if not isinstance(lname, str):
            raise TypeError("That is not a valid last name.")

        if not isinstance(title, str):
            raise TypeError("That is not a valid title.")

        # Predetermined set of pronouns available, separate checks for people who go by multiple, e.g. "he/they"
        if isinstance(pp, str):
            for j in pp.split("/"):
                if j.lower() not in pronouns:
                    raise TypeError("That is not a valid set of pronouns.")
        else:
            raise TypeError("That is not a valid set of pronouns.")

        if not isinstance(dob, str):
            raise TypeError("That is not a valid date of birth.")
        else:

            '''
            # Also could have done this, but I only realised after writing the stuff beforehand. Will keep both anyway.
            dob_check = dob.split("/")

            try:
                dt.datetime(int(dob_check[2]), int(dob_check[1]), int(dob_check[0]))
            except:
                raise TypeError("That is not a valid date of birth.")

            '''

            dob_check = dob.split("/")
            for i in range(len(dob_check)):
                dob_check[i] = int(dob_check[i])

            if dob_check[1] in [9, 4, 5, 6, 11] and dob_check[0] > 30:
                raise ValueError("That is not a valid date of the form DD/MM/YYYY")
            elif dob_check[1] == 2:
                if dob_check[2] % 4 == 0 and dob_check[0] > 29:
                    raise ValueError("That is not a valid date of the form DD/MM/YYYY")
                elif dob_check[2] > 28:
                    raise ValueError("That is not a valid date of the form DD/MM/YYYY")
            elif dob_check[0] > 31:
                raise ValueError("That is not a valid date of the form DD/MM/YYYY")

            if dob_check[2] > int(str(dt.now())[0:4]) or dob_check[2] < int(str(dt.now())[0:4]) - 100:
                raise ValueError("We do not allow clients who are over the age of 100.")

        if not isinstance(occupation, str):
            raise TypeError("That is not a valid occupation.")

        if not isinstance(bal, float) and not isinstance(bal, int):
            raise TypeError("That is not a valid balance.")

        if not isinstance(overlim, float) and not isinstance(overlim, int):
            raise TypeError("That is not a valid overdraft limit.")
        elif overlim < 0:
            raise ValueError("You cannot have a negative overdraft limit.")

        # Assign variables to the information, set balance and overdraft limit to float if integers are input
        self.fname = fname.title()
        self.lname = lname.title()
        self.title = title.title()
        self.pp = pp.lower()
        self.dob = dob
        self.occupation = occupation.title()
        self.bal = float(bal)
        self.overlim = float(overlim)

    def add(self):
        """
        Adds the client to the file if they do not already exist
        :return: False when not a duplicate client
        """
        # Checks the client does not already exist, adds them to the file if they don't
        with open("clients.csv", "r+") as file:
            duplicate = False
            read = file.readlines()
            for row in read:
                # testing values (I accidentally added a space)
                # print(read)
                # print(row)
                # print(row[0])
                # print(type(row[0].lower()))
                # print(self.fname.lower())
                # print(str(self.fname.lower)==str(row[0].lower()))

                row = row.split(",")
                # Assume there are not two people with the exact same first name, last name and birthday
                if self.fname.lower() == row[0].lower() and self.lname.lower() == row[1].lower() and self.dob == row[4]:
                    duplicate = True

            if not duplicate:
                file.write(f"{self.fname},{self.lname},{self.title},{self.pp},{self.dob},{self.occupation},"
                           f"{self.bal},{self.overlim}\n")

        return duplicate

    def edit(self, editor):
        """
        Edits the information of a single client

        :param editor: dictionary containing old value as the key directing to the new value
        :return: True upon success
        """
        with open("clients.csv", "r") as file, open("clientstemp.csv", "w") as tempfile:
            read = file.readlines()

            for row in read:
                row = row.split(",")
                keys = editor.keys()
                keys = list(keys)
                if row[0] == keys[0] and row[1] == keys[1] and row[4] == keys[4]:
                    tempfile.write(f"{editor[row[0]]},{editor[row[1]]},{editor[row[2]]},{editor[row[3]]},"
                                   f"{editor[row[4]]},{editor[row[5]]},{editor[row[6]]},{editor[row[7]]}\n")
                else:
                    row = ",".join(row)
                    tempfile.write(row)
                    tempfile.write("\n")

        with open("clients.csv", "a") as file, open("clientstemp.csv", "r") as tempfile:
            read = tempfile.readlines()
            file.truncate(0)

            for row in read:
                file.write(row)
                file.write("\n")

        os.remove("clientstemp.csv")
        return True

    def __str__(self):
        """
        :return: user-friendly string representation of the class Client
        """
        return "Client called {} {}".format(self.fname, self.lname)

    def __repr__(self):
        """
        :return: developer-friendly string representation of the class Client
        """
        return "Client({} {})".format(self.fname, self.lname)


def searchEdit(fname, lname, dob):
    """
    Searches for a client in the file using their first name, last name and date of birth.

    :param fname: first name input
    :param lname: last name input
    :param dob: date of birth input
    :return: the client's information and the row they are located in the file, returns None and 0 if client not found
    """
    with open("clients.csv", "r") as file:
        read = file.readlines()

        num = 0
        for row in read:
            row = row.split(",")
            # print(row[0], read)
            if fname.title() == row[0] and lname.title() == row[1] and dob == row[4]:
                return row, num
            num += 1

    return None, 0
