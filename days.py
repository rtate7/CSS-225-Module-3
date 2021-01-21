# Bob Tate
# 1/21/21
#
# Solution to Problem 7
# This program gets a day from the user where day 0 is Sunday
# and day 6 is Saturday. The program then gets a length of stay
# in days from the user and determines what day of the week the 
# user will return on.

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# track whether a successful caclulation has been performed using the 
# boolean variable done
valid_number_entered = False

error_message = "Invalid input. You must enter valid integers."

# keep trying to get valid input until calculation is complete
while not valid_number_entered:
  start_day = input("On what day (0-6 with 0 being Sunday and 6 being Saturday) are you arriving?: ")
  
  # use try/except statement to continue with gallons only if user enters a number
  # for start_day
  try: 
    int(start_day)
    valid_number_entered = True
  except:
    print(error_message)

  if valid_number_entered:
    # set valid_number_entered back to false for next check
    valid_number_entered = False
    length_of_stay = input("How long will you be staying?: ")
    
    # use try/except statement to continue with calculation only if user enters a number
    try:
      # by trying to convert radius to a float, we can tell if it's a numeric value
      # also use round() to limit float values to a max of 2 digits after decimal
      int(length_of_stay)

      # set valid_number_entered to true sice calculation is successfully completed
      valid_number_entered = True
    except:
      print(error_message)

leave_day = (int(start_day) + int(length_of_stay)) % 7

print(
  "If you arrive on a " +
  DAYS[int(start_day)] +
  " (day " +
  start_day +
  ") and stay for " +
  str(length_of_stay) + 
  " days, you will leave on a " +
  str(DAYS[int(leave_day)]) +
  " (day " +
  str(leave_day) +
  ")."
)