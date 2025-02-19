myList = [1,2,3,4,5]
print(myList[3:])

print(2*item for item in myList)

myList = list(range(10))
print(myList)

filtered = [item for item in myList if item % 2 == 0]
print(filtered)

myString = "Mario Lazzari senior full stack developer"
words = myString.split()
print(words)

def cleanWord(word):
    return word.replace(' ','').lower()

cleanedWords = [cleanWord(word) for word in words]
print(cleanedWords)