# Bob Tate
# 1/21/21
#
# This program asks the user for tehir name and greets them with their name.

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

