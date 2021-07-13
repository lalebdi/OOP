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