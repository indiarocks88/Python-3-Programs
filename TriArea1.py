"""
Program: Python 3 program to calculate the area of triangle.
Date: Thu, 25-03-2021
@author: Ankur Saxena
Platform: Windows 10 Pro/x64/Python 3.6/Vim editor
"""

# program start

# import python module
import os

os.system ("cls") # clear the console screen

width = float (input("Please enter the width of the triangle:\n"))
height = float (input("Please enter the height of the triangle:\n"))

# calculate area of the triangle
area = width * height / 2

# print result
print ("\nArea of the triangle is: ",area)

# program end

"""
save this file as "TriArea1.py"
execute: $ python TriArea1.py [hit Enter]
output:

Please enter the width of the triangle:
25
Please enter the height of the triangle:
5

Area of the triangle is:  62.5
"""

