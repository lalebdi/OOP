# Create generator function

def Items():
    print("First Item !")
    yield 15

    print("Second Item!!")
    yield 25

    print("Last Item!!")
    yield 40


newGenerate = Items()
# yield will return a value and pause the execution while maintaining the state. return will terminate the function
print(next(newGenerate))
print(next(newGenerate))
print(next(newGenerate))

# Using generator function with for loop
def newUpTo(x):
    for i in range(x):
        yield i


seq1 = newUpTo(7)
print(next(seq1))
print(next(seq1))
print(next(seq1))
print(next(seq1))