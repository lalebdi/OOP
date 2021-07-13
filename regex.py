import re

newTxt = "You can start learning Python"
x = re.search("^You.*Python", newTxt)

if x:
    print("Yes")
else:
    print("No")