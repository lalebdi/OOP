# Create generator function

def Items():
    print("First Item !")
    yield 15

    print("Second Item!!")
    yield 25

    print("Last Item!!")
    yield 40


newGenerate = Items()

print(next(newGenerate))
print(next(newGenerate))
print(next(newGenerate))