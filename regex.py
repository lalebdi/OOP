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

otherTxt = "Python is very easy"
z = re.search("\s", otherTxt)
print("The first white space index= ", z.start())

a = re.sub("\s", "$", otherTxt)
print(a)

txt = "Python is very very easy"
b = re.search("very", txt)
print(b.span())

# Searching for upper case C in the beginning of a word and prints its position
something = "Code with Python now"
c = re.search(r"\bC\w+", something)
print(c.span())
print(c.string)
print(c.group())