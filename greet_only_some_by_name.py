# Bob Tate
# 1/21/21
#
# Solution to Problem 3
# This program asks the user for their name and greets them with their name
# only if the user is either me (Bob Tate) or my professor (Dr. Tovar).

# Store accepted names in a constant array (list)
ACCEPTED_NAMES = [
  "Bob", 
  "Robert", 
  "Bob Tate", 
  "Robert Tate", 
  "Dr. Tovar", 
  "Dr. Antonio Tovar",
  "Dr. Antonio Tovar Moldonado",
  "Antonio Tovar Moldonado"
  ]

name = input("Please enter your name: ")
if name in ACCEPTED_NAMES: 
  # If user inputted name is on the list of accepted names, greet by name
  print("Hello, " + name + ".")
else: 
  # If user inputted name is not on the list of accepted names, issue a 
  # generic greeting
  print("Hello stranger!")

