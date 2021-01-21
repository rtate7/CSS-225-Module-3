# Bob Tate
# 1/21/21
#
# Solution to Problem 5
# This program asks the user for a number of miles driven and a number
# of gallons used and outputs the efficiency in mpg.

# track whether a successful caclulation has been performed using the 
# boolean variable done
def get_valid_float(input_message, error_message):
  valid_number_entered = False
  while not valid_number_entered:
    user_value = input(input_message)
    try: 
      float(user_value) != 0
      valid_number_entered = True
    except:
      print(error_message)
  return float(user_value)

error_message = "Invalid input. You must enter valid numbers greater than zero."

miles_input_string = "Please enter the number of miles driven: "
miles = get_valid_float(miles_input_string, error_message)

gallons_input_string = "Please enter the gallons: "
gallons = get_valid_float(gallons_input_string, error_message)

mpg = round(miles / gallons, 2)

print("You've travelled " +
  str(miles) + 
  " and used " + 
  str(gallons) + 
  " gallons for an efficiency of " + 
  str(mpg) + 
  " miles per gallon."
)