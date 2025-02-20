for n in range(1,101):
    if n%15 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else: # optional
        print(n)

# ternary operator
n = 5
print("even" if n%2 == 0 else "odd")