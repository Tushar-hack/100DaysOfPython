# File Handling : creating, reading, updating, and deleting files
import os
# Opening a File and writing to it

file = open("myProfile.txt", "w")
file.write("This is Tushar Tak. My age is 22.")
file.close()

# opening and reading through a file

f = open("myProfile.txt", "r")
content = f.read()
print(content)
f.close()

# Deleting a file
os.remove("myProfile.txt")

# Creating a file at another location
fileptr = open("../profile.txt", "w")
fileptr.write("This is new File in root folder.")
fileptr.close()

f = open("../profile.txt", "r")
content = f.read()
print(content)

f.close()

os.remove("../profile.txt")


