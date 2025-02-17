# if
a = True
b = True
c = True

if a:
    print('a is true')
    print('and print this too')
    if b:
        print('b is true')
        if c:
            print('c is true')     
else:
    print('a is false')

print('Always print this')

# for
a = [1,2,3,4,5]

for item in a:
    print(item)

print(4 in a)

# while
a = 0
while a < 5:
    print(a)
    a += 1