'''
A program that calculates and displays the amount earned based on the user
input hours worked and the rate per hour.

Name: Lucy Finnerty
Date: 6/10/24
'''

print("\nWelcome to earning calculation program.")
name = input("Please enter your full name: ")

print("\nHello,", name)
print("This program will ask you to enter the hours worked and the rate per hour. The program will\ncalculate and display the amount earned.\n")

hours = eval(input("Enter hours worked: "))
rate = eval(input("Enter rate per hour: "))
money = hours * rate
print("You have earned: ${:.2f}".format(money))

print("\nThank you and have a nice day.\nGoodbye!")