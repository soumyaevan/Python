class Chicken:
    total_eggs = 0
    def __init__(self,species,name):
        self.species = species
        self.name = name
        self.eggs = 0
        
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

#This is implemetation of Class Chciken in ClassDemo3.py
c1 = Chicken("Indian","Murgi")
c2 = Chicken("Chinese","Chinese_Murgi")
print(Chicken.total_eggs)
c1.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)