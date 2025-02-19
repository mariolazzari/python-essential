animalsList = ['cat', 'dog', 'elephant', 'lion', 'tiger']

animals = {item[0]: item[1] for item in enumerate(animalsList)}
print(animals)

animals = {key: value for key, value in enumerate(animalsList)}
print(animals)

list = list(animals.items())
print(list)