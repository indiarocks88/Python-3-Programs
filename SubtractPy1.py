"""
Program: Python 3 program to calculate and display the subtraction of two numbers entered by the user.
Date: Monday, 22-03-2021
@author: Ankur Saxena
Platform: Windows 10 Pro/x64/Python 3.6/Vim editor
"""

# program start

# importing python module
import os

os.system ("cls") # clear the console screen

# for Linux or MacOS, use "clear" command inside the 'system.os ()'

num1 = input ("Please enter first number:\n")
num2 = input ("Please enter second number:\n")

# calculating addition
result = int(num1) - int(num2) 

# printing result
print ("\n\nThe subtraction of {0} and {1} is: {2}" .format(num1, num2, result))

# program end

# Save this file as "SubtractPy1.py"
# Execute: $ python3 SubtractPy1.py [hit Enter]

"""
Output:

Please enter first number:
95
Please enter second number:
36


The subtraction of 95 and 36 is: 59
"""

