from copy import copy
class Human:
    def __init__(self,first,last,age):
        self._first = first
        self._last = last
        self._age = age
        
    def __repr__(self):
        return f"Human named {self._first} {self._last} of age {self._age}"
    
    def __add__(self,other):
        if isinstance(other,Human):
            return Human(first='Newborn',last=self._last,age=0)
        raise ValueError("Invalid Addition")
    
    def __mul__(self,other):
        if isinstance(other,int):
            return [copy(self) for i in range(other)]
        

soumya = Human("Soumya","Sen",25)
mou = Human("Moumita","Das",26)
print(soumya + mou)
print("--------------------------------------")
multi = (soumya+mou)*2
multi[0]._first = "Souryadeep"
multi[1]._first = "Soumita"
print(multi)