class Animal:
    def __init__(self,name,species):
        self._name = name
        self._species = species

    def __repr__(self):
        return f"{self._name} is a {self._species}"

    def make_sound(self,sound):
        print(f"{self._name} is doing sound of {sound}")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species='Dog')
        self._breed = breed

    def activity(self):
        print(f"{self._name} is running")

class Bird(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species='Bird')
        self._breed = breed

    def activity(self):
        print(f"{self._name} is flying")

    
rocky = Dog("Rocky","Pomerian")
piu = Bird("Piu","Parrot")
print(rocky)
rocky.make_sound("Barking")
rocky.activity()

print(piu)
piu.make_sound("Whistle")
piu.activity()
