"""
Program: Python 3 program to swap two numbers using * and /
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
num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print("\nAfter swapping, first number is: ", num1)
print("\nAfter swapping, second number is: ", num2)

# program end

# save this file as 'SwapTwoNo3.py'
# execute: $ python SwapTwoNo3.py [hit Enter]

"""
output:

Before swapping, first number is:  20

Before swapping, second number is:  30

After swapping, first number is:  30

After swapping, second number is:  20

Process finished with exit code 0
"""
