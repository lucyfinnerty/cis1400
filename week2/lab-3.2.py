'''
Gross Pay Calculator

This program will determine the gross pay and net payment for an employee when given 
hours worked and rate per hour.

Name: Lucy Finnerty
Date: 6/11/24
'''
# ask for user's name, hours worked, and rate per hour, so they can be set to variables used for manipulation
name = input("Full Name: ")
hours = eval(input("Hours worked: "))
rate = eval(input("Rate per hour: $"))

# if hours worked is less than or equal to 40, gross pay is simply hours multiplied by rate
if hours <= 40:
    gross_pay = hours * rate
    print("Gross Pay: $", gross_pay) # output gross pay
# if user worked more than the standard 40 hours, every additonal hour the user is payed 1.5 times their original rate
elif hours > 40:
    reg_hours = 40 # straight time capped at 40 hours
    overtime_hours = hours - reg_hours # subtract 40 from hours worked to find amount of overtime hours
    overtime_rate = rate * 1.5 # user payed 1.5 times origial rate for all hours worked in excess of 40
    gross_pay = (reg_hours * rate) + (overtime_hours * overtime_rate) # adds products of 40 hours * original rate and overtime hours * overtime rate
    print("Gross Pay: $", gross_pay) # output gross pay

# if gross pay is greater than 0, find net payment
if gross_pay > 0:
        taxes = gross_pay * .07 # taxes are 7% of gross pay
        net_pay = gross_pay - taxes # deduct taxes from gross pay to find net pay
        print("Net Payment: $", net_pay) # output net payment