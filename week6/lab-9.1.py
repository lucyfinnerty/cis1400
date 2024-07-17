'''
Rectangle Class

This class calculates area and perimeter of a rectangle given its width and height.

Name: Lucy Finnerty
Date: 7/16/24
'''
class Rectangle:
    # constructor that creates rectangle object with default values of 1 and 2 for width and height respectively
    def __init__(self, width = 1, height = 2):
        self.__width = width
        self.__height = height
    # function that calculates rectangle's area
    def getArea(self):
        # area = width * height
        return self.__width * self.__height
    # function that calculates rectangles's perimeter
    def getPerimeter(self):
        # perimeter = 2 * (width + height)
        return 2 * (self.__width + self.__height)
    # function that gets value of width variable
    def getWidth(self):
        return self.__width
    # function that gets value of height variable
    def getHeight(self):
        return self.__height
    # function to set the width to a value
    def setWidth(self, width):
        self.__width = width
    # function to set the height to a value
    def setHeight(self, height):
        self.__height = height

# test program that creates 2 rectangles

# enter width and height into constructor's parameters
rect1 = Rectangle(4, 40)
rect2 = Rectangle(3.5, 35.7)

# use get functions to retrieve values and calculations
# display results
print("Rectangle 1")
print("Width:", rect1.getWidth())
print("Height:", rect1.getHeight())
print("Area:", rect1.getArea())
print("Perimeter:", rect1.getPerimeter())

# use get functions to retrieve values and calculations
# display results
print("\nRectangle 2")
print("Width:", rect2.getWidth())
print("Height:", rect2.getHeight())
print("Area:", rect2.getArea())
print("Perimeter:", rect2.getPerimeter())