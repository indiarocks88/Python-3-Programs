"""
Program: Python 3 program to calculate the area of the circle.
Date: Thu, 25-03-2021
@author: Ankur Saxena
Platform: Windows 10 Pro/x64/Python 3.6/Vim editor
"""

# program start

# import python module
import os
import math
os.system ("cls") # clear the console screen

radius = float (input ("Please enter the radius of the circle:\n"))

# calculate area of the circle
circleArea = math.pi * radius * radius

# print result
print ("Area of the circle is: %.2f" %circleArea)

# program end

# save this file as "CirArea1.py"
# execute: $ python CirArea1.py [hit Enter]
"""
output:

Please enter the radius of the circle:
15
Area of the circle is: 706.86
"""

