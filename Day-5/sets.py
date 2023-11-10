# Sets : multiple item in single Variable
# Contain different type of data Types
myset = {"apple", "banana", "cherry", True, 1, 0}

animal = {"Dog", "Cow", "Horse"}

print(myset)
print(animal)
print(len(myset))
print(type(myset))

# Unordered, unchangeable, No duplicates

# Accessing an Item
for x in myset:
    print(x)

print("Dog" in animal)

# Adding sets to a set
animal.add("Goat")
# Add any iterable by update function
animal.update(myset)

print(animal)

# Removing an item from a set
animal.remove("Goat")
animal.discard(True)
print(animal)
# Remove item randomly
item1 = animal.pop()
print(item1)

# Deleting a set : del set_name

# Emptying a set : clear()
animal.clear()
print(animal)
