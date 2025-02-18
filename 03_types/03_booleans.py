# True
bool(1)
bool(0.1)
bool("a")
bool(1j)
bool("True")
bool([1])
bool({1})

# False
bool(1)
bool(0.0)
bool("")
bool(0j)
bool("False")
bool([])
bool({})

# Boolean logic
weatherNice = False
haveUmbrella = True

if haveUmbrella or weatherNice:
    print("Stay at home")
else:
    print("Go for a walk")

if (not haveUmbrella) and (not weatherNice):
    print("Stay at home")
else:
    print("Go for a walk")