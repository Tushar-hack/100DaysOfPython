# json is a module that help to store python data structure in json format and retrieve data in json

import json

f = open("data.json", "r")
jsonData = f.read()
f.close()
convertedData = json.loads(jsonData)

print(convertedData["name"])

fileptr = open("data.json", "a")
x = {
    "name": "Bhavesh",
    "age": 26,
    "city": "Ajmer",
    "Field": "Electrical"
}

jsonOfX = json.dumps(x, sort_keys=True)

fileptr.write(jsonOfX)
fileptr.close()

# opening and reading it

jsonFile = open("data.json", "r")
content = jsonFile.read()
print(content)
jsonFile.close()

# json modules has 2 function :
# Loads() which convert json -> python
# dumps() which convert python -> json
