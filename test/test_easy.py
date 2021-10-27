import unittest
import pytest
from pyleetcode.easy.easy import Easyfunctions
from pyleetcode.medium.medium import Mediumfunctions
from pyleetcode.hard.hard import Hardfunctions

#global insttance
Easy = Easyfunctions()
Medium = Mediumfunctions()
Hard = Hardfunctions()
class TestStringMethods(unittest.TestCase):
      
    def test_two_sum(self):
        nums = [2,7,11,15]
        target = 9
        self.assertAlmostEqual(Easy.twosum(nums, target), [0,1])
        
    def test_palindrome(self):
        pass




if __name__ == '__main__':
    unittest.main()