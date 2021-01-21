# Bob Tate
# 1/21/21
#
# Solution to Problem 4
# This program asks the user for a radius, calculates the area
# of a circle with that radius, and displays that area.

import input_validation
# need to import math so we can use math.pi
import math

input_message = "Please enter a radius: "
error_message = "Invalid input. You must enter a number."

radius = input_validation.get_valid_float(input_message, error_message)

# calculate area rounded to 2 decimal places
area = round(math.pi * radius**2, 2)
print("The area of a circle with radius: " + str(radius) + " is " + str(area) + ".")
