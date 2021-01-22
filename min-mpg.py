# Bob Tate
# 1/22/21
#
# Solution to Problem 5 - Minimum Requirement
# This program asks the user for a number of miles driven and a number
# of gallons used and outputs the efficiency in mpg.

miles = float(input("Please enter the number of miles driven: "))
gallons = float(input("Please enter the gallons: "))
mpg = miles / gallons

print("You've travelled " +
  str(miles) + 
  " and used " + 
  str(gallons) + 
  " gallons for an efficiency of " + 
  str(mpg) + 
  " miles per gallon."
)