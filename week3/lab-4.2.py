'''
Magic Date Calculator

This program asks a user to enter a month, day, and year to determine whether or not the date is magic.
A magic date is when the month times the day equals the year. Otherwise, it is not magic.

Name: Lucy Finnerty
Date: 6/25/24
'''

# ask user for a month
month = int(input("Please enter a month in numeric form: "))
# ensure user inputs a real month (jan - dec)
if not (1 <= month <= 12):
    print("Invalid input. Month must be between 1 and 12.") # display invalid input statement
    exit() # program stops
# ask user for a day (1st - 31st)
day = int(input("Please enter a day in numeric form: "))
# ensure user inputs a real day
if not (1 <= day <= 31):
    print("Invalid input. Day must be between 1 and 31.") # display invalid input statement
    exit() # program stops
# ask user for a year (xx00 - xx99)
year = int(input("Please enter the last two digits of a year: ")) # display invalid input statement
# ensure user inputs a real year
if not (0 <= year <= 99):
    print("Invalid input. Year must be between 00 and 99.") # display invalid input statement
    exit()# program stops

# if user inputs do not satisfy above conditions, then they are valid and program can continue to calculate numbers

# multiply the month and day and format by rounding
product = round(month * day)
# if the product is the same as the year the user inputed, the date is magic
if product == year:
    print("\nThis date is magic!")
else:
    print("\nThis date is not magic.")