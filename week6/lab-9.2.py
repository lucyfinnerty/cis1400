'''
Shipping Charges using Objects and Classes

This program has a ShippingCharges class that creates a contructor, makes mutator 
and accessor methods available for the parameters, calculates charges of a 
package based on its weight, and prints out the final data.

Name: Lucy Finnerty
Date: 7/16/24
'''
class ShippingCharges:

    # constructor with parameters of company name, user's name, number of packages, total weight, and total cost
    def __init__(self, company="Fast Freight Shipping Company", user_name="", num_packages=0, total_weight=0.0, total_cost=0.0):
        self.__company = company
        self.__user_name = user_name
        self.__num_packages = num_packages
        self.__total_weight = total_weight
        self.__total_cost = total_cost
    
    # mutator and accessor functions
    def getCompanyName(self):
        return self.__company
    def setCompanyName(self, company):
        self.__company = company
    def getUserName(self):
        return self.__user_name
    def setUserName(self, user_name):
        self.__user_name = user_name
    def getNumPackages(self):
        return self.__num_packages
    def setNumPackages(self, num_packages):
        self.__num_packages = num_packages
    def getTotalWeight(self):
        return self.__total_weight
    def setTotalWeight(self, total_weight):
        self.__total_weight = total_weight
    def getTotalCost(self):
        return self.__total_cost
    def setTotalCost(self, total_cost):
        self.__total_cost = total_cost

    # function packageCharge accepts weight as an argument and return the charges
    def packageCharge(self, weight):
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

    # function that prints data for the user
    def printSummary(self):
        print(f"\n{self.__company}")
        print(f"User: {self.__user_name}")
        print(f"Packages: {self.__num_packages}")
        print(f"Total weight: {self.__total_weight}")
        print(f"Total cost: ${self.__total_cost:.2f}")

''' end of ShippingCharges class '''

# the driver function that initiates the main program 
def main():
    # method 1: create an object instance with the default constructor, and then print the information.
    shipping1 = ShippingCharges()
    shipping1.setUserName("Default User")
    print("\nMethod 1: Default constructor")
    shipping1.printSummary()

    # method 2: create an object instance with the constructor’s parameters (hard-coded the values), and then print the information.
    shipping2 = ShippingCharges(user_name="Hardcoded User", num_packages=2, total_weight=10, total_cost=25)
    print("\nMethod 2: Constructor with parameters")
    shipping2.printSummary()

    # method 3: create another object by asking the user to enter multiple weights of packages until the user has no more packages to input. print the information when the user has completed the input values.
    shipping3 = ShippingCharges()
    user_name = input("\nHello, can I please get your full name?\n")
    shipping3.setUserName(user_name)
    
    # greet user and explain the program
    print("\nWelcome", user_name, "to the Fast Freight Shipping Company shipping rate program.\nThis program is designed to take your package(s) weight in pounds and\ncalculate how much it will cost to ship them based on the following rates.\n\n2 pounds or less = $1.10 per pound\nOver 2 pounds but no more that 6 pounds = $2.20 per pound\nOver 6 pounds but no more than 10 pounds = $3.70 per pound\nOver 10 pounds = $3.80 per pound\n")
    
    # initialze default numbers
    total_cost = 0.0
    total_weight = 0.0
    num_packages = 0
    while True:
        # prompt user to enter package weight
        weight = float(input("\nPlease enter your package weight in pounds: "))
        # cost set to number returned when calling weight into packageCharge function
        cost = shipping3.packageCharge(weight)
        # add cost and weight to their total variable, then increment num_packages
        total_cost += cost
        total_weight += weight
        num_packages += 1
        # display cost for singular package
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
        if more_packages == 'n':
            print(f"Thank you for your purchase, your total for today is ${shipping3.getTotalCost():.2f}\nGoodbye!")
            break # program ends
    
    # use mutator functions to set the new values
    shipping3.setNumPackages(num_packages)
    shipping3.setTotalWeight(total_weight)
    shipping3.setTotalCost(total_cost)

    # display results for method 3 -- program ends
    print("\nMethod 3: User input")
    shipping3.printSummary()

# run the main function
if __name__ == "__main__":
    main()