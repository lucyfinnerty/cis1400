'''
Shape Generator

This program has three shape classes -- Cube, Circle, and Square. Each has a contructor with default
values for objects to be created. As well as accessor and mutator functions for said parameters. The
program asks a user to select an option of how they would like to receive their results -- by 
printing to console, saving to file of user's choice, or through a GUI window. When they pick one of
the three options, they receive the name and area of ten random shapes (combination of the three).

Name: Lucy Finnerty
Date: 7/29/24
'''
import math
import random
from tkinter import*

'''
Cube class allows for a Cube object to be created. It has a constructor with default parameters for length, width,
and height. There are accessor and mutator functions for said parameters. As well as functions to calculate the 
shape's area and display the shape's name.
'''
class Cube:
    # default contructor for a Cube object - length, height, width = 3.0
    def __init__(self, length=3.0, width=3.0, height=3.0):
        self.__length = length
        self.__width = width
        self.__height = height

    # accessor and mutator functions for length, width, and height
    def getLength(self):
        return self.__length
    def setLength(self, length):
        self.__length = length
    def getWidth(self):
        return self.__width
    def setWidth(self, width):
        self.__width = width
    def getHeight(self):
        return self.__height
    def setHeight(self, height):
        self.__height = height

    # function to find surface area of a cube
    def findArea(self):
        return 2 * (self.__length * self.__width + self.__length * self.__height + self.__width * self.__height)
    # function to display the name of the shape - Cube
    def display(self):
        return "Cube"
'''
Circle class allows for a Circle object to be created. It has a constructor with a default parameter for radius.
There are accessor and mutator functions for said parameter. As well as functions to calculate the shape's area 
and display the shape's name.
'''
class Circle:
    # default constructor for a Circle object - radius = 4.3
    def __init__(self, radius=4.3):
        self.__radius = radius

    # accessor and mutator functions for radius
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius

    # function to find area of a circle
    def findArea(self):
        return math.pi * (self.__radius * self.__radius)
    # function to display the name of the shape - Circle
    def display(self):
        return "Circle"
'''
Square class allows for a Square object to be created. It has a constructor with a default parameter for side length.
There are accessor and mutator functions for said parameter. As well as functions to calculate the shape's area 
and display the shape's name.
'''
class Square:
    # default constructor for a Square Object - side length = 4.0
    def __init__(self, side_length=4.0):
        self.__side_length = side_length

    # accessor and mutator functions for side length
    def getSideLength(self):
        return self.__side_length
    def setSideLength(self, side_length):
        self.__side_length = side_length

    # function to find area of a square
    def findArea(self):
        return self.__side_length * self.__side_length
    # function to display the name of the shape - Square
    def display(self):
        return "Square"
    
# function to generate a list of 10 cube, circle, and/or square objects
def randomGenerator():
    # create shapes list
    shapes = []
    # loop 10 times
    for i in range(10):
        # type will randomly be set to 0, 1, or 2
        type = random.randint(0,2)
        # type = 0 --> circle object
        if type == 0:
            shapes.append(Circle())
        # type = 1 --> square object
        if type == 1:
            shapes.append(Square())
        # type = 2 --> cube object
        if type == 2:
            shapes.append(Cube())
    return shapes

# function to write the results into a file of the user's choice
def save(shapes):
    # ask user for name of file
    filename = input("Enter the name of the file to save your result: ")
    # open file in write mode
    f = open(filename, "w")
    # iterate over each shape in shapes list
    for shape in shapes:
        # display name of shape
        shape.display()
        # write results to file user entered
        f.write(f"{shape.__class__.__name__}, {shape.findArea():.2f}\n")
    # print to console when successful    
    print(f"Results saved to {filename}")

# function to print out name and area of shape from shapes list
def displayShapes(shapes):
    # iterate over each shape in shapes list
    for shape in shapes:
        # display name and area of shape
        print(f"{shape.display()}, {shape.findArea():.2f}")
    print("\n")

# function that creates a GUI window to display the shape and its information
def guiWindow(shapes):
    # create window with title "Results" and size of 250x250
    window = Tk()
    window.title("Results")
    window.geometry("250x250")
    # iterate over each shape in shapes list
    for shape in shapes:
        # variable set to shape's name and area print statement
        shape_info = f"{shape.display()}, {shape.findArea():.2f}"
        # create label with shape_info text in window
        label = Label(window, text=shape_info)
        # add label to window
        label.pack()
    # start the GUI program
    window.mainloop()

# main function that starts the program, creates list, displays welcoming statement, prompts user to select an option, and displays closing statement
def main():
    # create list of 10 random circle, cube, and/or square objects
    shapes = randomGenerator()
    # display welcoming statement
    print("Welcome to my Shape Generator!")
    # while user enters a valid input...
    while True:
        # print options to user for selection
        print("Please select which option to run the program:\n1. Save results to a file\n2. Print results on screen\n3. Print results inside GUI window\n4. Exit")
        # variable set to user's input
        choice = input("\nEnter: ")
        print("\n")
        # choice = 1 --> write results to file
        if choice == '1':
            # call save function
            save(shapes)
        # choice = 2 --> display results to console
        elif choice == '2':
            #call displayShapes function
            displayShapes(shapes)
        # choice = 3 --> display results to a GUI window
        elif choice == '3':
            # call guiWindow function
            guiWindow(shapes)
        # choice = 4 --> program ends
        elif choice == '4':
            # display closing statement
            print("Bye! Program Terminating.")
            break
        else:
            # print error statement, prompt user to enter valid number
            print("Invalid choice, please enter a number (1-4).")
    return

# run main function
if __name__ == "__main__":
    main()