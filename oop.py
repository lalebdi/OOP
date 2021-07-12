class Instructors:
    companyName = "Upper West Side"

    def __init__(self, course):
        self.course = course

    def printInfo(self):
        print("My company name is", self.companyName)


elearning = Instructors("Python")
inPerson = Instructors("Java")

elearning.printInfo()
print(elearning.course)