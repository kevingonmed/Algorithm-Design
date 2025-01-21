import json
"""data = {
    "name": "Python",
    "designer": "Guido van Rossum",
    "paradigm": ["imperative", "object-oriented", "functional"],
    "year": 1991
}

text = json.dumps(data)
with open ("Lab02.json", "w") as file:
    file.write(text)

with open ("Lab02.json", "r") as file:
    data = file.read()
    data2 = json.loads(data)
    print(data)"""

with open ("Lab02.json", "r") as file:
    data = file.read()
    print (data)
    