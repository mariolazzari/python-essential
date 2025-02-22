class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def getLegs(self):
        return self._legs
       
    def bark(self):
        print(f'{self.name} says woof!')

dog = Dog('Rex')
dog.bark()  # Rex says woof!
print(dog.name)  # Rex
print(dog.getLegs())  # 4

