def factorial(num):
    if num < 0 or type(num)!=int:
        return None
    
    if num < 2:
        return 1
    
    fact = 1
    count = 1

    while count <= num:
        fact *= count
        count += 1

    return fact


def factorial2(num):
    if num < 0 or type(num)!=int:
        return None
    
    if num == 0:
        return 1
    
    return num * factorial2(num -1)
        
print(factorial(0))
print(factorial(5.1))
print(factorial(-5))
print(factorial(5))

print(factorial2(0))
print(factorial2(5.1))
print(factorial2(-5))
print(factorial2(5))
