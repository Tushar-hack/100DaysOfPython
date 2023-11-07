# Defining a List
fruits = ["Apple", "Banana", "Cherry"]
animals = list(("Cow", "Dog", "Horse"))
print(fruits)
print(animals)

# Key Features : Ordered ,Changeable ,Allow Duplicates
print(len(fruits))
print(type(fruits))

# Accessing a List
print(fruits[0])
# Negative indexing means start from the end
print(fruits[-1])

# Slicing a new List => It will create a new list of that items
print(fruits[0:2])

# Checking an Item in list
if "Cow" in animals:
    print("Cow is Present in the Farm.")

# Changing an item in list
fruits[1] = "Kiwi"
print(fruits)

# Inserting an Item at an index
fruits.insert(1, "Banana")
print(fruits)

# Adding Items
fruits.append("Orange")
print(fruits)

# Adding other lists and other data Structure to the list
fruits.extend(animals)
print(fruits)
fruit_tuple = ("Pear", "Chiku")
fruits.extend(fruit_tuple)
print(fruits)

# Removing an Item from List
# Method 1
fruits.remove("Kiwi")
print(fruits)

# Method 2 : Removing from any index
fruits.pop(0)
print(fruits)

# Method 3
del fruits[0]
print(fruits)

# del and clear are also used to delete a list completely

# Looping the List
for fruit in fruits:
    print(fruit)

# for i in range(len(fruits)):
#     print(fruits[i])
#     i += 1

# List Comprehension
print([x.upper() for x in fruits if x == "Cherry"])

# Sorting a List
fruits.sort(reverse=True)
print(fruits)

# copying a List
new_fruits = fruits.copy()
print(new_fruits)

# Joining the List
list1 = ["Tushar", "Rahul", "Bhavesh"]
list2 = ["26", "23", "34"]

list3 = list1 + list2
print(list3)



