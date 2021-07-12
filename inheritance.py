class Person:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def printName(self):
        print(self.firstName, self.lastName)

florist = Person("Jane", "Doe")

florist.printName()


class Lawyers(Person): # if you create a child class without a constructor, it will inherit all methods and attributes
    pass


immigration_lawyer = Lawyers("John", "Blah")

immigration_lawyer.printName()