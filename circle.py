# Bob Tate
# 1/21/21
#
# Solution to Problem 4
# This program asks the user for a radius, calculates the area
# of a circle with that radius, and displays that area.

# need to import math so we can use math.pi
import math

# track whether a successful caclulation has been performed using the 
# boolean variable done
done = False

# keep trying to get valid input until calculation is complete
while not done:
  radius = input("Please enter a radius: ")

  # use try/except statement to continue with calculation only if user enters a number
  try:
    # by trying to convert radius to a float, we can tell if it's a numeric value
    float(radius)

    area = math.pi * float(radius)**2
    print("The area of a circle with radius: " + radius + " is " + str(area) + ".")

    # set done to true sice calculation is successfully completed
    done = True
  except:
    print("Invalid input. You must enter a number.")