"""
Program: Python program to find the area of a rectangle.
Date: Fri, 26-03-2021
@author: Ankur Saxena
Platform: Windows 10/x64/Python 3.6/Vim editor
"""

# program start

# import python module
import os

os.system ("cls") # clear the console screen

# for linux or macos users, use "clear" command inside the "os.system()" function

# take input from the user
width = float (input ("Please enter width of the rectangle:\n"))
height = float (input ("Please enter height of the rectangle:\n"))

# calculate area of rectangle
area = width * height

# print result
print ("\nThe area of the rectangle is: ", area)

# program end

# save this file as "RectArea1.py"
# execute: $ python RectArea1.py [hit Enter]

"""
output:

Please enter width of the rectangle:
25
Please enter height of the rectangle:
5

The area of the rectangle is:  125.0

Press ENTER or type command to continue
"""

