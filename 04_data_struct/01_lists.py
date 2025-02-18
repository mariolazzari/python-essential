myList = [1,2,3,4,5]
print(myList[3:])
print(myList[0:6:2])
print(myList[0:6:3])
print(myList[::2])

for i in range(10):
    print(i)

myList = list(range(10))
print(myList)

myList.append(10)
myList.insert(5, "five")
print(myList)
myList.remove("five")
print(myList)

myList.pop()
print(myList)

myListCopy = myList.copy()

while len(myList):
    myList.pop()

print(myList)
print(myListCopy)
