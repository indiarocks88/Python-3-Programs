"""
Program: Python program to calculate and display the area of a Ellipse.
Date: Fri, 26-03-2021
@author: Ankur Saxena
Platform: Windows 10 Pro/x64/Python 3.6/Vim editor
"""

"""
Formula, Area of a Ellipse = pi * a * b

where,
--> a is the distance from the center to a vertex.
--> b is the distance from the center to a co-vertex.
"""

# program start

# import python module
import os

os.system ("cls") # clear the console screen

# for linux or macos users, use "clear" command inside the "os.system()" function

# take imput from the user
a = float (input ("Please enter the value of a:\n"))
b = float (input ("Please enter the value of b:\n"))
# calculate area of ellipse
# pi = 3.14

# calculate area of ellipse
pi = 3.14
ellipseArea = pi * a * b

# print result
print ("\nArea of the Ellipse is: ", ellipseArea)

# program end

# save this file as "EllipseArea1.py"
# execute: $ EllipseArea1.py [hit Enter]

"""
output:

Please enter the value of a:
6
Please enter the value of b:
2

Area of the Ellipse is:  37.68

Press ENTER or type command to continue
"""

