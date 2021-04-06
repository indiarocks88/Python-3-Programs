"""
Program: Python 3 program to swap two numbers without using third variable.
Date: Tue, 6-4-2021
@author: ANKUR SAXENA
Platform: Windows 10 Pro/x64/Python 3.6/VS Code
"""

# program start
# import python module
import os

os.system("cls") # clear the console screen

num1 = 20
num2 = 30

print("\nBefore swapping, first number is: ", num1)
print("\nBefore swapping, second number is: ", num2)

# swap numbers
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# print result
print("\nAfter swapping, first number is: ", num1)
print("\nAfter swapping, second number is: ", num2)

# save this file as 'SwapTwoNo2.py'
# execute: $ python SwapTwoNo2.py [hit Enter]

"""
output:

Before swapping, first number is:  20

Before swapping, second number is:  30

After swapping, first number is:  30

After swapping, second number is:  20

Process finished with exit code 0
"""
