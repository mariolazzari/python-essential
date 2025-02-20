items = [1, 2, 3, 4, 5]

for item in items:
    print(item)

animalLookups = {
   "a": ["ant", "ape", "apple"],
   "b": ["bat", "bear", "beetle"],
   "c": ["cat", "camel", "crab"],
   "d": ["dog"]
}

for letter, animals in animalLookups.items():
    print(f"Animals that start with {letter.upper()}:")
    for animal in animals:
        print(f"  {animal}")

for letter, animals in animalLookups.items():
    if len(animals) > 1:
        continue
    print("Only one animal starts with", animals)

for letter, animals in animalLookups.items():
    if len(animals) > 1:
        print("Only one animal starts with", animals)
        break

for number in range(2, 100):
    for factor in range(2, int(number **2)+1):
        if number % factor == 0:
            print(f"{number} equals {factor} * {number//factor}")
            break
    else:
        print(f"{number} is a prime number")