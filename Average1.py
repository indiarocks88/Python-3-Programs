"""
Program: Python 3 program to find the average of two numbers entered by the user.
Date: Thu, 1-4-2021
@author: Ankur Saxena
Platform: Windows 10/x64/Python 3.6/Vim editor
"""

# formula to find the average = sum of all numbers / number of items

# program start
# import python package
import os

os.system ("cls") # clear the console screen

num1 = float (input ("Please enter first number:\n"))
num2 = float (input ("Please enter second number:\n"))

# calculate average
avg = (num1+num2)/2

# print result
print ("\nThe average of ",num1, " and ",num2, " is: ",avg)

# program end

# save this file as "Average1.py"
# execute: $ python Average1.py [hit Enter]

"""
output:

Please enter first number:
25.0
Please enter second number:
8.5

The average of  25.0  and  8.5  is:  16.75

Press ENTER or type command to continue
"""

