'''
Number Calc using File I/O

Name: Lucy Finnerty
Date: 7/8/24
'''

import os

# user is asked
while True:
    fileName = input("Please enter file name with path (or 'exit'): ")
    if fileName == 'exit':
        print("Goodbye!")
        break
    if fileName.strip():
        if os.path.isfile(fileName):
            fp = open(fileName,"r")
            s = fp.read()
            numbers = [ eval(x) for x in s.split() ] 

            if numbers:
                total = sum(numbers)
                count = len(numbers)
                average = round(total / count)
                smallest = min(numbers)
                largest = max(numbers)

                print(f"\nThe smallest value is {smallest}")
                print(f"The largest value is {largest}")
                print(f"There are a total of {count} numbers")
                print(f"The sum of all the numbers is {total}")
                print(f"The average is {average}\n")
            else:
                print("\nFile is empty\n")
        else:
            print(f"\n{fileName} does not exist\n")
    else:
        print("\nPlease enter a valid file name\n")