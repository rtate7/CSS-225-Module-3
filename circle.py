# Bob Tate
# 1/21/21
#
# Solution to Problem 4
# This program asks the user for a radius, calculates the area
# of a circle with that radius, and displays that area.

def get_valid_float(input_message, error_message):
  valid_number_entered = False
  while not valid_number_entered:
    user_value = input(input_message)
    try: 
      float(user_value)
      valid_number_entered = True
    except:
      print(error_message)
  return float(user_value)

# need to import math so we can use math.pi
import math

input_message = "Please enter a radius: "
error_message = "Invalid input. You must enter a number."

radius = get_valid_float(input_message, error_message)

# calculate area rounded to 2 decimal places
area = round(math.pi * radius**2, 2)
print("The area of a circle with radius: " + str(radius) + " is " + str(area) + ".")
