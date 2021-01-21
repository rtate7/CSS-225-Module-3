# Bob Tate
# 1/21/21
#
# Solution to Problem 6
# This program asks the user for a temperature in Fahrenheit and
# converts to Celsius.

import input_validation

error_message = "Invalid input. You must enter a valid number."
input_message = "Please enter the temperature in degrees Fahrenheit: "
fahrenheit = input_validation.get_valid_float(input_message, error_message)
celsius = (fahrenheit - 32) * 5.0/9.0
  
# display the result of the calculation rounded to 2 decimals
print(str(fahrenheit) + "F is the same as " + str(round(celsius, 2)) + "C")

