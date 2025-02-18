import math

name = 'Mario Lazzari'
print(name[0])

firstName = name[0:5]
print(firstName)

firstName = name[:5]
print(firstName)

lastName = name[6:]
print(lastName)

list = [1,2,3,4,5]
print(list[2:4])
print(len(list))
print(len(name))

# formatting (f'')
print('My number is ' + str(5))
print(f'My number is {5}')
print(f'My number is {5} and twice is {2*5}')

print(f'pi = {math.pi}')
print(f'pi = {math.pi:.2f}')
print('pi = {}'.format(math.pi))

# multi lines
my_text = '''
    Hi Mario,
        how are you today?

    Have a nice day
'''

print(my_text)