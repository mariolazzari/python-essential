# lambda
(lambda x: x**2)(2)
print((lambda x: x**2)(2))

myList = [{"n":1}, {"n":5}, {"n":2}]
sorted = sorted(myList, key=lambda x: x['n'])
print(sorted)