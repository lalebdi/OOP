class Person:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def printName(self):
        print(self.firstName, self.lastName)

florist = Person("Jane", "Doe")

florist.printName()