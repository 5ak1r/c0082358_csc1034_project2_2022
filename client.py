from datetime import datetime as dt
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

        if not isinstance(fname, str):
            raise TypeError("That is not a valid first name.")
        if not isinstance(lname, str):
            raise TypeError("That is not a valid last name.")
        if not isinstance(title, str):
            raise TypeError("That is not a valid title.")
        if not isinstance(pp, str):
            raise TypeError("That is not a valid set of pronouns.")
        if not isinstance(dob, str):
            raise TypeError("That is not a valid date of birth.")
        else:
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

            if dob_check[2] > int(str(dt.now())[0:4]) or dob_check[2] < int(str(dt.now())[0:4])-100:
                raise ValueError("We do not allow clients who are over the age of 100.")
        if not isinstance(occupation, str):
            raise TypeError("That is not a valid occupation.")
        if not isinstance(bal, float) and not isinstance(bal, int):
            raise TypeError("That is not a valid balance.")
        if not isinstance(overlim, float) and not isinstance(bal, int):
            raise TypeError("That is not a valid overdraft limit.")

        self.fname = fname
