import unittest
from robotics import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man",battery=50)
        
    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)
        
    def test_say_name(self):
        self.assertEqual(self.mega_man.say_name(),"Hi! BEEP BEEP!!! My name is Mega Man.")
        

if __name__ == "__main__":
    unittest.main()