# Dictionary stores Key:value Pair
profile = {
    "name": "Tushar",
    "age": 23,
    "Field": "Computer Science"
}
profile2 = dict(
    name="Rikku",
    age=40,
    Field="Teacher"
)
print(profile2)
print(profile)
print(type(profile))

# Changeable, Not allow duplicate, Ordered

# Accessing a single item
print(profile["name"])
print(profile.get("name"))

# Methods of Dictionary
# Return a List
print(profile.keys())
print(profile.values())
# return tuples in a list
print(profile.items())


# checking for key
if "name" in profile:
    print("Yes")

