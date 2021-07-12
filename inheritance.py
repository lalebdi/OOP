class Person:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def printName(self):
        print(self.firstName, self.lastName)

florist = Person("Jane", "Doe")

florist.printName()


class OldLawyers(Person): # if a child class created without a constructor, it will inherit all methods and attributes
    pass


immigration_lawyer = OldLawyers("John", "Blah")

immigration_lawyer.printName()


class Lawyers(Person):
    def __init__(self, firstname, lastname, caseType):
        Person.__init__(self, firstname, lastname)
        self.caseType = caseType

    def printInfo(self):
        print(self.firstName, self.lastName, self.caseType)


civil_lawyer = Lawyers("Smiley", "Teeth 😁", "civil")
civil_lawyer.printInfo()

