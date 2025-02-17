class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ": Bau")

tudor = Dog("Tudor")
bart = Dog("Bart")

tudor.speak()
bart.speak()