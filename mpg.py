# Bob Tate
# 1/21/21
#
# This program asks the user for a number of miles driven and a number
# of gallons used and outputs the efficiency in mpg.

# track whether a successful caclulation has been performed using the 
# boolean variable done
valid_number_entered = False

error_message = "Invalid input. You must enter valid numbers greater than zero."

# keep trying to get valid input until calculation is complete
while not valid_number_entered:
  miles = input("Please enter the number of miles driven: ")
  
  # use try/except statement to continue with gallons only if user enters a number
  # for miles
  try: 
    float(miles)
    valid_number_entered = True
  except:
    print(error_message)

  if valid_number_entered:
    # set valid_number_entered back to false for next check
    valid_number_entered = False
    gallons = input("Please enter the gallons: ")
    
    # use try/except statement to continue with calculation only if user enters a number
    try:
      # by trying to convert radius to a float, we can tell if it's a numeric value
      # also use round() to limit float values to a max of 2 digits after decimal
      mpg = round(float(miles) / float(gallons), 2)

      # set valid_number_entered to true sice calculation is successfully completed
      valid_number_entered = True
    except:
      print(error_message)
      
print("You've travelled " +
  str(miles) + 
  " and used " + 
  str(gallons) + 
  " gallons for an efficiency of " + 
  str(mpg) + 
  " miles per gallon."
)