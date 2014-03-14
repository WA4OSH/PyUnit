#-------------------------------------------------------------------------------
# Name:        pyunit.py
# Purpose:     This file contains the sample unittest cases
#
# Author:      Konrad Roeder
# Notes:       http://pyunit.sourceforge
#              runs under python 3.3.4
#
# Created:     03/14/2014
# Licence:     CC0 1.0 Universal
#-------------------------------------------------------------------------------

import unittest                   #use built-in unittest library
from math_unit import add         #use only the add and multiply methods
from math_unit import multiply    #from the library math_unit.py

# Setup, teardown and test cases
class AddTest(unittest.TestCase):

   def setUp(self):
      '''Verify environment is setup properly''' # Printed if setup fails
      pass


   def tearDown(self):
      '''Verify environment is torn down properly''' # Printed if teardown fails
      pass


   def test_positive_add(self):
      '''Verify that adding positive numbers works''' # Printed if test fails
      self.assertEqual(add(10,23,22), 55)
      self.assertEqual(add(11,23), 34)
      self.assertEqual(add(1,1,17), 19)


   def test_negative_add(self):
      '''Verify that adding negative numbers works''' # Printed if test fails
      self.assertEqual(add(-12,23), 11)


   def test_negative_add_skip(self):
      self.skipTest
      '''Verify that skipping tests works''' # Printed if test fails
      self.assertEqual(add(-12,23), 11)


   def test_positive_multiply(self):
      '''Verify that multiplying numbers works''' # Printed if test fails
      self.assertEqual(multiply(4,6), 24)


   def test_divide(self):
      '''Verify that dividing numbers works''' # Printed if test fails
      self.assertEqual(divide(4,6), 24)

if __name__=='__main__':
   unittest.main()
