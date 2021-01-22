# Bob Tate
# 1/22/21
#
# Solution to Problem 6 - Minimum Requirement
# This program asks the user for a temperature in Fahrenheit and
# converts to Celsius.

input_message = "Please enter the temperature in degrees Fahrenheit: "
fahrenheit = float(input("Please enter the temperature in degrees Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0/9.0
  
# display the result of the calculation
print(str(fahrenheit) + "F is the same as " + str(celsius) + "C")

