# Bob Tate
# 1/22/21
#
# Solution to Problem 4 - Minimum Requirement
# This program asks the user for a radius, calculates the area
# of a circle with that radius, and displays that area.

import math

radius = input("Please enter a radius: "
area = math.pi * float(radius) ** 2
print("The area of a circle with radius: " + str(radius) + " is " + str(area) + ".")