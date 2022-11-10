from datetime import datetime as dt
import csv
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

        self.fname = fname.title()
        self.lname = lname.title()
        self.title = title.title()
        self.pp = pp.lower()
        self.dob = dob
        self.occupation = occupation.title()
        self.bal = float(bal)
        self.overlim = float(overlim)

        with open("clients.csv", "a+") as file:
            read = csv.reader(file)
            write = csv.writer(file)
            for row in read:
                # Assume there are not two people with the exact same first name, last name and birthday
                print(self.fname)
                print(row[0])
                if self.fname == row[0] and self.lname == row[1] and self.dob == row[4]:
                    raise ValueError("That person already exists.")

            write.writerow([self.fname, self.lname, self.title, self.pp, self.dob, self.occupation,
                           self.bal, self.overlim])


    def edit(self, editor):

        with open("clients.csv", "r") as file, open("clientstemp.csv", "w") as tempfile:
            read = csv.reader(file)
            write = csv.writer(tempfile)

            for row in read:
                keys = editor.keys()
                keys = list(keys)
                if row[0] == keys[0] and row[1] == keys[1] and row[4] == keys[4]:
                    write.writerow([editor[row[0]], editor[row[1]], editor[row[2]], editor[row[3]], editor[row[4]],
                                   editor[row[5]], editor[row[6]], editor[row[7]]])
                else:
                    write.writerow(row)

        with open("clients.csv", "w") as file, open("clientstemp.csv", "r") as tempfile:
            write = csv.writer(file)
            read = csv.file(tempfile)

            for row in read:
                write.writerow(row)

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
