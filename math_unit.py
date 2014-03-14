#-------------------------------------------------------------------------------
# Name:        math_unit.py
# Purpose:     Code to be tested by unittest.py
#
# Author:      Konrad Roeder
# Notes:       http://pyunit.sourceforge
#              runs under python 3.3.4
#
# Created:     03/14/2014
# Licence:     CC0 1.0 Universal
#-------------------------------------------------------------------------------

# Code under test

def add(a,b,c=0):
    return a+b-c   #broken on purpose

def subtract(a,b):
    return a-b

def multiply(a,b,c=0):
    return a*b*c   #broken on purpose

def divide(a,b):
    return a/b
