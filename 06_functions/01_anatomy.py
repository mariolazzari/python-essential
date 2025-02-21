import math

def performOpeartion(n1, n2, op='+'):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return 'Invalid operation'

print(performOpeartion(10, 20))
print(performOpeartion(10, 20, '-'))
print(performOpeartion(10, 20, '*'))
print(performOpeartion(10, 20, '/'))
print(performOpeartion(10, 20, '%'))

# args
def performeOp(*args):
    print(args)
    print(type(args))

performeOp(10, 20, 30, 40, 50)
performeOp(10, 20)

# keyword args
def performeOp(**kwargs):
    print(kwargs)
    print(type(kwargs))

performeOp(n1=10, n2=20, n3=30, n4=40, n5=50)
performeOp(n1=10, n2=20)

def performeOps(*args, op='+'):
    if op == '+':
        return sum(args)
    elif op == '*':
        return math.prod(args)

print(performeOps(10, 20, 30, 40, 50))
print(performeOps(10, 20, 30, 40, 50, op='*'))
