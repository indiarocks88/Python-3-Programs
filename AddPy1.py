"""
Program: Python 3 program to calculate and display the addition of two numbers entered by the user.
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
result = int(num1) + int(num2) # type casting

# printing result
print ("\n\nThe addition of {0} and {1} is: {2}" .formax(num1, num2, result))

# program end

# Save this file as "AddPy1.py"
# Execute: $ python3 AddPy1.py [hit Enter]

"""
Output:

Please enter first number:
45
Please enter second number:
45


The addition of 45 and 45 is: 90
"""

