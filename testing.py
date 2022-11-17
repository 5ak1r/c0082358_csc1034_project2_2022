from client import *

try:
    dob_error = Client("Sakir", "Azimkar", "Mr", "He/Him", "30/06/1674", "Student", 300, 500)
except ValueError:
    print("This raises a ValueError as expected")

try:
    fname_error = Client("$akir", "Azimkar", "Mr", "He/Him", "22/10/2001", "Student", 300, 500)
except ValueError:
    print("This raises a ValueError as expected")

try:
    pp_error = Client("Sakir", "Azimkar", "Mr", "this is not a set of pronouns", "22/10/2001", "Student", 300, 500)
except ValueError:
    print("This raises a ValueError as expected")

try:
    fname_type_error = Client(123, "Azimkar", "Mr", "he/him", "22/10/2001", "Student", 300, 500)
except TypeError:
    print("This raises a TypeError as expected")

try:
    lname_error = Client("Sakir", "Azimk@r", "Mr", "he/him", "22/10/2001", "Student", 300, 500)
except ValueError:
    print("This raises a ValueError as expected")

try:
    case_sens = Client("sAKiR", "aZiMkaR", "Mr", "HE/HIM", "22/10/2001", "stUdEnT", 300, 500)
    print(case_sens.fname, case_sens.lname, case_sens.title, case_sens.pp, case_sens.occupation)
except ValueError:
    print("An error was raised that should not have been")
else:
    print("No error was raised")

try:
    bal_error = Client("Sakir", "Azimkar", "Mr", "he/him", "22/10/2001", "Student", "300", 500)
except TypeError:
    print("This raises a TypeError as expected")

try:
    del_error = Client("This", "Client", "Does", "he/him", "22/10/2001", "Not Exist", 0, 0)
    del_error.delete()
except ValueError:
    print("This raises a ValueError as expected")
