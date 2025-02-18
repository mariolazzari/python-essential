from decimal import Decimal, getcontext

res = 20 / 5
print(type(res)) # int / int = float

res = 4 + 4.0
print(type(res)) # int + float = float

res = 4 ** 2
print(type(res)) # exp int = int

res = 4.0 ** 2
print(type(res)) # exp flot = float

# casting
print(int(8.99999)) # 8

# round
print(round(14 / 3)) # 5
print(round(14 / 3, 2)) # 4.67

# string to int
print(int("2")) # 2
print(int("100", 2)) # 4
print(int("ab", 16)) # 171

# decimale
print(1.2 - 1.0) # 0.19999999999999996

getcontext().prec = 1
print(Decimal(1.2) - Decimal(1.0)) # 0.2




