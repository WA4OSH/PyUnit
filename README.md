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
5) There is an error because the divide funtion does not load because it was not imported from math_unit. Correct
   the error by either adding a "from math_unit import divide" line into the test code, or by skipping 
   the test.
6) There is a test failure because the formula to add three numbers has an error in it.  The other test failure
   is because the formula to multiply numbers when called with two numbers has an error in it.  Eliminate the 
   failures by correcting the code in the math_unit.py file.
7) Run the unittests again.  They should pass.


   

