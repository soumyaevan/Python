class ElectricCar:
    def __init__(self,model,color):
        self._model = model
        self._color = color

#Following functions define the engine mechanism
    def run(self):
        return f"{self._model} is running on electric"
    
    @property
    def color(self):
        return self._color
class DieselCar:
    def __init__(self,model,color):
        self._model = model
        self._color = color

    def run(self):
        return f"{self._model} is running on diesel"
    
    @property
    def color(self):
        return self._color

class Audi(ElectricCar,DieselCar):
    def __init__(self,model,color):
        super().__init__(model,color)

myAudi = Audi("v8.0","Black")
print(f"Audi of {myAudi.color} color and model {myAudi.run()}")
