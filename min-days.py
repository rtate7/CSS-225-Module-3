# Bob Tate
# 1/22/21
#
# Solution to Problem 7 - Minimum Requirement
# This program gets a day from the user where day 0 is Sunday
# and day 6 is Saturday. The program then gets a length of stay
# in days from the user and determines what day of the week the 
# user will return on.

start_day = input("On what day (0-6 with 0 being Sunday and 6 being Saturday) are you arriving?: ")
length_of_stay = input("How long will you be staying?: ")

# by taking modulo (%) 7, we get the number of days left over after full weeks are removed
leave_day = (int(start_day) + int(length_of_stay)) % 7

print(
  "If you arrive on day " +
  start_day +
  " and stay for " +
  length_of_stay + 
  " days, you will leave on day " +
  str(leave_day) +
  "."
)