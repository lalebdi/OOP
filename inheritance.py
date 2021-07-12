class Person:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def printName(self):
        print(self.firstName, self.lastName)

florist = Person("Jane", "Doe")

florist.printName()


class OldLawyers(Person): # if you create a child class without a constructor, it will inherit all methods and attributes
    pass


immigration_lawyer = OldLawyers("John", "Blah")

immigration_lawyer.printName()


class Lawyers(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        # self.firstName = firstname
        # self.lastName = lastname

    def printInfo(self):
        print(self.firstName, self.lastName)

civil_lawyer = Lawyers("Simely", "Teeth")
civil_lawyer.printInfo()