'''
Shipping Charges

This program will display shipping and total charges based on the weight of item/s and 
their rate per pound.

Name: Lucy Finnerty
Date: 6/11/24
'''
# output intro
print("Fast Freight Shipping Company total shipping charge calculator:")
# set weight to user input
weight = eval(input("Enter weight of package in pounds: "))


if weight <= 2:
    rate = 1.10 # rate is $1.10
    total = weight * rate # total is weight multiplied by rate
    print("Rate per pound: $", rate, "\nTotal charge: $", total) # output shipping and total charges

# if weight is greater than 2 pounds, but less than or equal to 6 pounds...
elif weight > 2 and weight <= 6:
    rate = 2.20 # rae is $2.20
    total = weight * rate # total is weight multiplied by rate
    print("Rate per pound: $", rate, "\nTotal charge: $", total) # output shipping and total charges

# if weight is greater than 6 pounds, but less than or equal to 10 pounds...
elif weight > 6 and weight <= 10:
    rate = 3.70 # rate is $ 3.70
    total = weight * rate # total is weight multiplied by rate
    print("Rate per pound: $", rate, "\nTotal charge: $", total) # output shipping and total charges

# if weight is greater than 10..
elif weight > 10:
    rate = 3.80 # rate is $3.80
    total = weight * rate # total is weight multiplied by rate
    print("Rate per pound: $", rate, "\nTotal charge: $", total) # output shipping and total charges