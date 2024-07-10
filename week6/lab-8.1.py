'''
Number Calc using File I/O

This program that will loop and ask the user to enter a file name. When the file name is 
entered, the program will read its content and compute the sum, and average of all numbers 
stored in the file. The smallest value, largest value, and the number of numbers read 
from the file will be also be displayed. The program verifies the existence of all the data 
files to be read and prints an error message if the file you are attempting to access a file
that does not exist.

Name: Lucy Finnerty
Date: 7/8/24
'''

import os

# infinite loop to repeatedly ask user to enter a file name with its path, until the user enters 'exit'
while True:
    # file name with path is stored in fileName
    fileName = input("Please enter file name with path (or 'exit'): ")
    # if user enters 'exit' to be stored in fileName, closing statement displayed and program breaks
    if fileName == 'exit':
        print("Goodbye!")
        break
    # check if fileName is empty or not
    if fileName.strip():
        # check whether path is an existing file
        if os.path.isfile(fileName):
            fp = open(fileName,"r") # open file in read mode
            s = fp.read() # read entire contents of file into s
            numbers = [ eval(x) for x in s.split() ] # split contents into individual numbers
            fp.close()  # close file

            # if list of numbers is not empty
            if numbers:
                # calculate sum, amount of numbers, average, min, and max numbers
                total = sum(numbers)
                count = len(numbers)
                average = round(total / count)
                smallest = min(numbers)
                largest = max(numbers)
                
                # display results
                print(f"\nThe smallest value is {smallest}")
                print(f"The largest value is {largest}")
                print(f"There are a total of {count} numbers")
                print(f"The sum of all the numbers is {total}")
                print(f"The average is {average}\n")
            else:
                # if file exists, but no content
                print("\nFile is empty\n")
        else:
            # file does not exist at provided path
            print(f"\n{fileName} does not exist\n")
    else:
        # if user does not enter a file and path
        print("\nPlease enter a valid file name\n")