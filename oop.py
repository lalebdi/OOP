class Instructors:
    companyName = "Upper West Side"

    def __init__(self, course, duration):
        self.course = course
        self.duration = duration

    def printInfo(self):
        print("My company name is", self.companyName)


elearning = Instructors("Python", 3)
inPerson = Instructors("Java", 2)

elearning.printInfo()
print(elearning.course)
print(inPerson.duration)

inPerson.course = "Django"

print(inPerson.course)

# DEL elearning.duration