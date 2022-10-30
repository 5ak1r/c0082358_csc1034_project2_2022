class Client:

    # Creates a class
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("That is not a name")

        self.name = name

