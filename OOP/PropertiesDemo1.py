class Human:
    def __init__(self,first,last,age):
        self._first = first
        self._last = last
        if age>=0:
            self._age = age
        else:
            raise(ValueError("Invalid Age"))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_val):
        if new_val>=0:
            self._age = new_val
        else:
            raise ValueError("Age can not be negative!")

Soumya = Human("Soumya","Sen",25)
print(Soumya.age)
Soumya.age = 25.6
print(Soumya.age)