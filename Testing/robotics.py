class Robot:
    def __init__(self, name, battery=50, skill=[]):
        self.name = name
        self.battery = battery
        self.skill = skill
        
    def charge(self):
        self.battery = 100
        
    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"Hi! BEEP BEEP!!! My name is {self.name}."
        return f"No charge!!! Please plug into charger."
    
    def learn_skill(self, skill):
        if self.battery > 5:
            self.skill.append(skill)
            self.battery -= 5
            return self.skill
        return f"Not enough charge left to learn new skill!"