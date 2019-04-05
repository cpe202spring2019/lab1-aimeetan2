# Name: Aimee Tan
# Course: CPE 202, Spring 2019
# Assignment: Lab 1 Tests

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Used to check with list of integers."""
        self.assertEqual(max_list_iter([2, 3, 1]), 3)

        """Used to check with empty list"""
        self.assertEqual(max_list_iter([]), None)
        
        """Used to check for ValueError."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)


    def test_reverse_rec(self):
        """Used to check with list of more than one integer."""
        self.assertEqual(reverse_rec([1, 2, 3]),[3, 2, 1])

        """Used to check with list of one integer."""
        self.assertEqual(reverse_rec([1]), [1])

        """Used to check for ValueError."""
        int_list = None
        with self.assertRaises(ValueError):
            reverse_rec(int_list)


    def test_bin_search(self):
        """Used to check when target is middle value."""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)

        """Used to check when target is less than middle value."""
        self.assertEqual(bin_search(2, 0, 4, [1, 2, 3, 4, 5]), 1)

        """Used to check when target is greater than middle value."""
        self.assertEqual(bin_search(4, 0, 4, [1, 2, 3, 4, 5]), 3)
    
        """Used to check when target is not found."""
        self.assertEqual(bin_search(2, 0, 5, [1, 3, 4, 5, 6, 7]), None)

        """Used to check for ValueError."""        
        int_list = None
        with self.assertRaises(ValueError):
            bin_search(2, 0, 5, int_list)


if __name__ == "__main__":
        unittest.main()

    
