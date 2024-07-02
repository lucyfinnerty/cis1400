'''
Volume and Surface Area Calculator

This program calculates the volume and side surface of a cylinder with a given radius and
length respectively. 

Name: Lucy Finnerty
Date: 7/2/24
'''

import math

def cylVol (radius, length):
    volume = math.pi * (radius * radius) * length
    return volume

def surfArea (radius, length):
    surfArea = 2 * math.pi * radius * length
    return surfArea

radius = eval(input("Enter radius of cylinder: "))
length = eval(input("Enter length of cylinder: "))

volume = cylVol(radius, length)
surfArea = surfArea(radius, length)

print("The volume of your cylinder is", volume)
print("The side surface area of your cylinder is", surfArea)