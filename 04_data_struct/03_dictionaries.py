# Dictionaries
from collections import defaultdict

animals ={
    "dog": "bark",
    "cat": "meow",
    "cow": "moo",
    "pig": "oink"
}

print(animals["dog"])
animals["dog"] = "woof"
print(animals["dog"])

print(animals.keys())
print(animals.values())

listKeys = list(animals.keys())
listValues = list(animals.values())     
print(listKeys)
print(listValues)

print(animals.get("elephant", "no such animal"))
print(animals.get("dog", "no such animal"))
print(len(animals))

if "elephant" not in animals:
    animals["elephant"] = []

animals["elephant"].append("trumpet")
print(animals["elephant"])

animals = defaultdict(list)
animals["elephant"].append("trumpet")
print(animals["elephant"])

animals = defaultdict(lambda: "unknown")
print(animals["elephant"])
print(animals["dog"])   
print(animals)