import re

newTxt = "You can start learning Python"
x = re.search("^You.*Python$", newTxt) # starts with You and ends with Python

if x:
    print("Yes")
else:
    print("No")


anotherTxt = "Python is very very very easy"
y = re.findall("very", anotherTxt)
print(y)

