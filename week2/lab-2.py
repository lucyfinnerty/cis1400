'''
Two-in-One

This program will convert feet to meters and display the result. As well as
calculating and displaying the area of a triangle when given the base and height values.

Name: Lucy Finnerty
Date: 6/11/24
'''

# set feet to user input
feet = eval(input("Number in feet: "))

# if feet is greater than or equal to 0...
if feet >= 0:
    # multiply feet by 0.305 to convert to meters
    meters = feet * 0.305
    # output conversion to user
    print("Meters =", meters)

# set base and height to user input
base = eval(input("Enter the base of a Triangle: "))
height = eval(input("Enter the height of a Triangle: "))

# if base and height are greater than or equal to 0...
if base >= 0 and height >= 0:
    # multiply half of the base by height to get the area
    area = (base * 0.5) * height
    # output area of triangle to user
    print("The area is", area)