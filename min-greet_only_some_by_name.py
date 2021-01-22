# Bob Tate
# 1/22/21
#
# Solution to Problem 3 - Minimum Requirement
# This program asks the user for their name and greets them with their name
# only if the user is either me (Bob Tate) or my professor (Dr. Tovar).

name = input("Please enter your name: ")
if name == "Bob" or name == "Dr. Tovar": 
  print("Hello, " + name + ".")
else: 
  # generic greeting
  print("Hello stranger!")
  