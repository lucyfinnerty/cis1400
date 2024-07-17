'''
Shipping Calculator with Functions

This program asks for a user's name, greets them, then calculates and displays how much each 
package will cost to ship and the total cost of all packages.

Name: Lucy Finnerty
Date: 7/3/24
'''

# ask the user’s full name, greet, and explain to the user what the program is all about. 
def greeting():
    # asks and stores user's name to variable
    name = input("Hello, can I please get your full name?\n")
    # display introduction and shipping charges using user's name
    print("\nWelcome", name, "to the Fast Freight Shipping Company shipping rate program.\nThis program is designed to take your package(s) weight in pounds and\ncalculate how much it will cost to ship them based on the following rates.\n\n2 pounds or less = $1.10 per pound\nOver 2 pounds but no more that 6 pounds = $2.20 per pound\nOver 6 pounds but no more than 10 pounds = $3.70 per pound\nOver 10 pounds = $3.80 per pound\n")

# function packageCharge accepts weight as an argument and return the charges
def packageCharge(weight):
    # determine rate based on weight
    if weight <= 2:
        rate = 1.10
    elif weight > 2 and weight <= 6:
        rate = 2.20
    elif weight > 6 and weight <= 10:
        rate = 3.70
    else: # weight > 10
        rate = 3.80

    # calculate and return cost for the package
    cost = weight * rate
    return cost

# the driver function that initiates the main program 
def main():
    # calls greeting and packageCharge functions
    greeting()
    total_cost = 0.0
    while True:
        # prompt user to enter package weight
        weight = float(input("\nPlease enter your package weight in pounds: "))
        cost = packageCharge(weight)
        total_cost += cost

        # display cost of current package
        print(f"Your cost is: ${cost:.2f}")

        # loop runs indefinitely until valid input is received by user, then action is taken and loop breaks
        while True:
            # give user the option to add another package
            more_packages = input("Would you like to ship another package <y/n> ?: ")
            if more_packages.lower() == 'y' or more_packages.lower() == 'n': # in case user capitalizes their answer, use .lower()
                break
            else: # anything other than y or n
                print("Invalid input") # display message and user can try again
    
        # if user does not have a another package, display closing message and give them total cost
        if more_packages.lower() == 'n':
            print(f"Thank you for your purchase, your total for today is ${total_cost:.2f}\nGoodbye!") # Exit loop if user does not want to ship more packages
            break # program ends

# run the main function
if __name__ == "__main__":
    main()