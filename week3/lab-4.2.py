'''
Magic Date Calculator

This program asks a user to enter a month, day, and year to determine whether or not the date is magic.
A magic date is when the month times the day equals the year. Otherwise, it is not magic.

Name: Lucy Finnerty
Date: 6/25/24
'''
'''
# ask user for a month, day, and year
month = int(input("Please enter a month in numeric form: "))
day = int(input("Please enter a day in numeric form: "))
year = int(input("Please enter the last two digits of a year: "))

# ensure user inputs real days, months, years
if not (1 <= month <= 12):
    print("Invalid input. Month must be between 1 and 12.")
elif not (1 <= day <= 31):
    print("Invalid input. Day must be between 1 and 31.")
elif not (0 <= year <= 99):
    print("Invalid input. Year must be between 0 and 99.")
else:
    # multiply the month and day
    product = round(month * day)
'''

while True:
    try:
        month = int(input("Please enter a month in numeric form (1-12): "))
        day = int(input("Please enter a day in numeric form (1-31): "))
        year = int(input("Please enter the last two digits of a year (00-99): "))

        # Validate inputs
        if not (1 <= month <= 12):
            print("Invalid input. Month must be between 1 and 12.")
            continue  # Restart the loop to prompt for input again

        if not (1 <= day <= 31):
            print("Invalid input. Day must be between 1 and 31.")
            continue  # Restart the loop to prompt for input again

        if not (0 <= year <= 99):
            print("Invalid input. Year must be between 0 and 99.")
            continue  # Restart the loop to prompt for input again

        break  # Exit the loop if all inputs are valid

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

# multiply the month and day
product = round(month * day)

# if the product is the same as the year the user inputed, the date is magic
if product == year:
    print("\nThis date is magic!")
else:
    print("\nThis date is not magic")