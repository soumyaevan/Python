import unittest
from Python.Testing.activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
    	"""eat should have a positive message for healthy eating"""
    	self.assertEqual(
			eat("broccoli", isHealthy=True),
			"I'm eating broccoli, because my body is a temple"
    	)
    def test_eat_unhealthy(self):
    	"""eat should indicate you've given up for eating unhealthy"""
    	self.assertEqual(
			eat("pizza", isHealthy=False),
			"I'm eating pizza, because YOLO!"
    	)
    
    def test_nap_number(self):
        with self.assertRaises(ValueError):
            nap("one")
     
    def test_short_nap(self):
        self.assertEqual(
			nap(1),"I am feeling refreshed after my 1 hour nap."
    	)
    def test_long_nap(self):
        self.assertEqual(
			nap(3),"Ugh!!! I overslept. 3 hours are too much."
		)
    

if __name__ == "__main__":
    unittest.main()