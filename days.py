# Bob Tate
# 1/21/21
#
# Solution to Problem 7
# This program gets a day from the user where day 0 is Sunday
# and day 6 is Saturday. The program then gets a length of stay
# in days from the user and determines what day of the week the 
# user will return on.

import input_validation

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

error_message = "Invalid input. You must enter an integer value."
start_day_message = "On what day (0-6 with 0 being Sunday and 6 being Saturday) are you arriving?: "
start_day = input_validation.get_valid_int(start_day_message, error_message)

length_of_stay_message = "How long will you be staying?: "
length_of_stay = input_validation.get_valid_int(length_of_stay_message, error_message)

leave_day = (start_day + length_of_stay) % 7

print(
  "If you arrive on a " +
  DAYS[start_day] +
  " (day " +
  str(start_day) +
  ") and stay for " +
  str(length_of_stay) + 
  " days, you will leave on a " +
  DAYS[leave_day] +
  " (day " +
  str(leave_day) +
  ")."
)