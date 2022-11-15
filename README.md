# c0082358_csc1034_project2_2022

Overview
---------
The purpose of this project is to use OOP to create a banking application that manages the following
client information: first name, last name, title, preferred pronouns, date of birth, occupation, balance
and overdraft limit. This application has the ability to view all clients' information or search for 
clients using their full name, date of birth or if they have a negative balance. You can also search for a
unique client using a combination of their full name and date of birth. This is because, as also mentioned
below, the application assumes that two clients can not have the same full name and date of birth.
Additional functionality includes the ability to edit (including their balance) or delete a client's 
information, or add the information of new clients to the system. Since the application uses file handling,
none of this data is lost when the application is closed, as all information is stored externally in a csv
file. Furthermore, if a client goes into debt, and the magnitude of their debt is greater than their
overdraft, then they will be charged the given £5 additional cost.

Assumptions
-----------
- All string entries are case insensitive
- There cannot exist two clients with the same full name and date of birth

How to Run the Application and Specific Example Use Case
--------------------------------------------------------
I decided to add a GUI to help with testing. In order to run the application using the GUI, you simply
need to run main.py and the rest is very self-explanatory.

To use the application without the GUI, you start by creating a client object with the following command:

```
client_object_name = Client(first_name, last_name, title, preferred_pronouns, date_of_birth, balance, overdraft_limit)
```

Following this line, you can then add, edit or delete the client information to/from the file using the
following methods:

```
client_object_name.add()
client_object_name.edit(dict)
client_object_name.delete()
```
Our example client shall be a woman named Janet Wilkinson. To define them into an object, we use the
following line:

```
Janet = Client("Janet", "Wilkinson", "Mrs", "she/her", "22/12/1984", "Doctor", 43421.23, 2000.00)
```

This defines a class object called Janet to be the information regarding our client. The constructor
completes all the verification of the inputs to make sure everything that we have entered is valid
information. For example, a number cannot be included in the name of the client, so an error would be 
raised if this was attempted.

Once we have created our client, we need to add them to the csv file, in order to keep their data when the
program ends. Initially, I was going to include this as part of the constructor, but this wasn't very
useful when I was building the GUI, so I decided to move it into a separate method. To add our client to
the file, we simply write

```
Janet.add()
```

Now say we want to edit some information about our client. The argument passed through edit is a 
dictionary. The keys of the dictionary consist of the old data regarding the client, whereas the value the
key assigned to is the new data to be replaced. For example, if I have the Janet client, and I want to 
change her last name to "Johnson" (our figurative client has just gotten married), and I want to reduce her 
balance by £1.23 (she has just purchased a drink while on her honeymoon) I would write:

```
Janet.edit({"Janet":"Janet
            "Wilkinson":"Johnson"
            "Mrs":"Mrs"
            "she/her":"she/her"
            "22/12/1984":"22/12/1984"
            "Doctor":"Doctor"
            43421.23:43420.00
            2000.00:2000.00})
```

The reason I chose a dictionary over something easier was that it was the easiest way I could think of (at 
the time of coding) to do it while also using some Tkinter functions I had already written for the
previous methods.

Now that Janet Johnson has gotten married and enjoyed her honeymoon, it is time to manage her finances
with her new partner. As such, she wants to delete her account with her current bank and set up a joint
account with her partner. So we want to remove all of Janet's information from our file as she no longer
uses our bank. To do this, we write

```
Janet.delete()
```

Although the Janet class still exists right now, when the program finishes it will be deleted. However,
her information has already been removed from the file, so she will be completely forgotten if someone else
runs the program again at a later date.