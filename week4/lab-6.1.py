'''
Volume and Surface Area Calculator

This program calculates the volume and side surface of a cylinder with a given radius and
length respectively. 

Name: Lucy Finnerty
Date: 7/2/24
'''

import math

# function that calculates a cylinder's volume based on its radius and length
def cylVol (radius, length):
    volume = math.pi * (radius * radius) * length # volume equation --> 3.14 * r^2 * L
    return volume

# function that calculates a cylinder's side surface area based on its radius and length
def surfArea (radius, length):
    surfArea = 2 * math.pi * radius * length # surface area of side equation --> 2 * 3.14 * r * L
    return surfArea

# ask user for radius and length of their cylinder for calculations
radius = eval(input("Enter radius of cylinder: "))
length = eval(input("Enter length of cylinder: "))

# variables volume and surfArea are set to the final calculated number that is returned from the funtions called
volume = cylVol(radius, length)
surfArea = surfArea(radius, length)

# displays final outputs to user
print("The volume of your cylinder is", volume)
print("The side surface area of your cylinder is", surfArea)