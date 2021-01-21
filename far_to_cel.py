# Bob Tate
# 1/21/21
#
# This program asks the user for a temperature in Fahrenheit and
# converts to Celsius.

# track whether a successful caclulation has been performed using the 
# boolean variable done
valid_number_entered = False

error_message = "Invalid input. You must enter a valid number."

# keep trying to get valid input until calculation is complete
while not valid_number_entered:
  fahrenheit = input("Please enter the temperature in degrees Fahrenheit: ")
  
  # use try/except statement to continue with gallons only if user enters a number
  # for miles
  try: 
    celsius = (float(fahrenheit) - 32) * 5.0/9.0
    valid_number_entered = True
  except:
    print(error_message)
      
# display the result of the calculation rounded to 2 decimals
print(str(fahrenheit) + "F is the same as " + str(round(celsius, 2)) + "C")