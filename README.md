PyUnit
======

Demo Code for the unittest library, which is PyUnit version bundled with Python since version 2.1

Files:
math_unit.py - The python code under test
pyunit.py - The unittest test cases

Procedure:
1) Install python 3.3.4 and PyScripter 2.5.3.0 on a windows machine
2) Put the python code math_unit.py and pyunit.py into a directory together
3) Open both math_unit.py and pyunit.py in PyScripter.
4) Then run the pyunit.py code.  It will call the unittest library and execute the tests.
   Note the results in the python interpreter window.
   
>>> 
E..FF
======================================================================
ERROR: test_divide (__main__.AddTest)
Verify that dividing numbers works
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Downloads\pyunit.py", line 55, in test_divide
    self.assertEqual(divide(4,6), 24)
NameError: global name 'divide' is not defined

======================================================================
FAIL: test_positive_add (__main__.AddTest)
Verify that adding positive numbers works
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Downloads\pyunit.py", line 32, in test_positive_add
    self.assertEqual(add(10,23,22), 55)
AssertionError: 11 != 55

======================================================================
FAIL: test_positive_multiply (__main__.AddTest)
Verify that multiplying numbers works
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Owner\Downloads\pyunit.py", line 50, in test_positive_multiply
    self.assertEqual(multiply(4,6), 24)
AssertionError: 0 != 24

----------------------------------------------------------------------
Ran 5 tests in 0.033s

FAILED (failures=2, errors=1)
Exit code:  True
>>>




5) There is an error because the divide funtion does not load because it was not imported from math_unit. Correct
   the error by either adding a "from math_unit import divide" line into the test code, or by skipping 
   the test.
6) There is a test failure because the formula to add three numbers has an error in it.  The other test failure
   is because the formula to multiply numbers when called with two numbers has an error in it.  Eliminate the 
   failures by correcting the code in the math_unit.py file.
7) Run the unittests again.  They should pass.


   

