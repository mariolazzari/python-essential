# Sets
mySet = {1,2,3}
print(mySet)

mySet = set(('a', 'b', 'c'))
print(mySet)

myList = ["a", "b", "c", "d", "e", "e", "d", "c", "b", "a"]
mySet = set(myList)
print(mySet)

myList = list(mySet)
print(myList)
print('a' in mySet)
print(len(mySet))

mySet.discard('a')
print(mySet)

while len(mySet):
    print(mySet.pop())

print(len(mySet))

# Tuples
myTuple = ('a', 'b', 'c')
print(myTuple)
print(myTuple[1])

def returnMultiple():
    return 1,2,3

print(type(returnMultiple()))

a,b,c = returnMultiple()
print(a)
print(b)
print(c)