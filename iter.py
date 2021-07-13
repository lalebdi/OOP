# Iterator from the fruits and print each value
fruits = ("Banana", "Apple", "Lemon")
newiter = iter(fruits)

print(next(newiter))
print(next(newiter))
print(next(newiter))

# Iterator for a sequence of characters

fruit = "Kiwi"
striter = iter(fruit)

print(next(striter))
print(next(striter))
print(next(striter))

# Build an iterator that returns numbers

class Counting:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 19:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

newObj = Counting()
# print(newObj)
objiter = iter(newObj)
# print(objiter)

for i in objiter:
    print(i)

# print(next(objiter))
# print(next(objiter))
# print(next(objiter))