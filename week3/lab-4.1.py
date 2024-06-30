'''
Shipping Charges Calculator

This program calculates and displays how much each package will cost to ship and the total cost of all packages.

Name: Lucy Finnerty
Date: 6/25/24
'''
# display introduction and shipping charges
print("Welcome to the Fast Freight Shipping Company shipping rate program.\nThis program is designed to take your package(s) weight in pounds and\ncalculate how much it will cost to ship them based on the following rates.\n")
print("2 pounds or less = $1.10 per pound\nOver 2 pounds but no more that 6 pounds = $2.20 per pound\nOver 6 pounds but no more than 10 pounds = $3.70 per pound\nOver 10 pounds = $3.80 per pound\n")

# initialize total cost 
total_cost = 0.0

while True:
    # prompt user to enter package weight
    weight = eval(input("\nPlease enter your package weight in pounds: "))

    # determine rate based on weight
    if weight <= 2:
        rate = 1.10
    elif weight > 2 and weight <= 6:
        rate = 2.20
    elif weight > 6 and weight <= 10:
        rate = 3.70
    elif weight > 10:
        rate = 3.80

    # calculate cost for current package
    cost = weight * rate
    # add current package cost to total cost
    total_cost += cost

    # display cost of current package
    print(f"Your cost is: ${cost:.2f}")

    # give user the option to add another package
    while True:
        more_packages = input("Would you like to ship another package <y/n> ?: ")
        if more_packages.lower() == 'y' or more_packages.lower() == 'n': # in case user capitalizes their answer, use .lower()
            break
        else: # anything other than y or n
            print("Invalid input") # display message and user can try again
    
    # if user does not have a another package, display closing message and give them total cost
    if more_packages.lower() == 'n':
        print(f"Thank you for your purchase, your total for today is ${total_cost:.2f}\nGoodbye!") # Exit loop if user does not want to ship more packages
        break # program ends