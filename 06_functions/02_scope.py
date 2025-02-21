def performOperation(*args, **kwargs):  
    print(args)
    print(kwargs)

print(performOperation(1,2, operation='add'))

# locals
def performLocals(n1, n2, op="add"):
    print(locals())

print(performLocals(1,2, op='add'))

# globals
print(globals())

message = "global message"

def func1(a,b):
    print(message)
    print(locals())

def func2(a,b):
    localMsg = "local message"
    print(message)
    print(locals())

func1(1,2)
func2(3,4)

# inner functions
def outer():
    x = 1
    def inner():
        print("inner:", x)
    inner()

print(outer())