# Defining a Tuple : Ordered, Unchangeable, Allow Duplicates
name = ("Tushar", "Bhavesh", "Atul")
print(name)
print(type(name))

# Accessing, Negative Index, Item Exist, looping, Joining all are same as Lists

# Modification in Tuple

# converting tuple into list
list_ofname = list(name)
# Do modification
list_ofname.append("Maya")
# convert back to tuple
name = tuple(list_ofname)
print(name)

# Unpacking a Tuple
name1, *name2 = name
print(name1)
# Remaining tuple would be converted into list
print(name2)


