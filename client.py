from datetime import datetime as dt

class Client:

    # Creates a class
    def __init__(self, fname, lname, title, pp, dob, occupation, bal, overlim):
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
            dob_check = dob.split("/")
            if dob_check[1].int() in [9,4,5,6,11] and (dob_check[0].int() > 30 or (dob_check[2].int()>dt.now()[0:4].int() or dob_check[2].int()<(dt.now()[0:4].int()-100))):
                raise ValueError("That is not a valid date of the form DD/MM/YYYY")
            elif dob_check[1].int() == 2 and dob_check[0].int() > 28:
                if dob_check[2] % 4 != 0 and (dob_check[0].int() > 29 or (dob_check[2].int()>dt.now()[0:4].int() or dob_check[2].int()<(dt.now()[0:4].int()-100))):
                    raise ValueError("That is not a valid date of the form DD/MM/YYYY")
            elif dob_check[0].int() > 31 or (dob_check[2].int()>dt.now()[0:4].int() or dob_check[2].int()<(dt.now()[0:4].int()-100)):
                raise ValueError("That is not a valid date of the form DD/MM/YYYY")
        if not isinstance(occupation, str):
            raise TypeError("That is not a valid occupation.")
        if not isinstance(bal, float):
            raise TypeError("That is not a valid balance.")
        if not isinstance(overlim, float):
            raise TypeError("That is not a valid overdraft limit.")


        self.name = fname