# Name: Aimee Tan
# Course: CPE 202, Spring 2019
# Assignment: Lab 1, Part 0 Tests

import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_init(self): 
        loc1 = Location("SLO", 35.3, -120.7)
        
        self.assertEqual(loc1.name, "SLO")
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7)


    def test_eq(self):              
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc2

        self.assertEqual(loc2, loc3)        


    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)

        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
