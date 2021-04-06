"""
Program: Python 3 program to swap two numbers.
Date: Tue, 6-4-2021
@author: ANKUR SAXENA
Platform: Windows 10 Pro/x64/Python 3.6/VS Code
"""

# program start
# import python module
import os

os.system ("cls") # clear the concole screen

num1 = 20
num2 = 30

print ("\nBefore swapping, first number is: ", num1)
print ("\nBefore swapping, second number is: ", num2)

# swap numbers
# value of num1 is assigned to num3
num3 = num1
# value of num2 is assigned to num1
num1 = num2
# value of num3 is assigned to num2
num2 = num3

# print result
print ("\nAfter swapping, first number is: ", num1)
print ("\nAfter swapping, second number is: ", num2)

# program end

# save this file as 'SwapTwoNo1.py'
# execute: $ python SwapTwoNo1.py [hit Enter]
"""
output:

Before swapping, first number is:  20

Before swapping, second number is:  30

After swapping, first number is:  30

After swapping, second number is:  20
"""
