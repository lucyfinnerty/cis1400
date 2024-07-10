'''
Ticketing System using File I/O

This program should read tickets and prices from ticket.txt; find minimum, maximum, and
average ticket prices and output the report into a file called output.txt.

Name: Lucy Finnerty
Date: 7/9/24
'''

import os

input_file = r'C:\git\cis1400\week6\ticket.txt'
output_file = 'output.txt'

if not os.path.isfile(input_file):
    print(f"Error: {input_file} not found")
else:
    fp = open(input_file,"r")
    lines = fp.readlines()
    ticket_prices = [float(line.split()[1]) for line in lines[1:] if line.strip()]

    if ticket_prices:
        num_tickets = len(ticket_prices)
        max_price = max(ticket_prices)
        min_price = min(ticket_prices)
        avg_price = sum(ticket_prices) / num_tickets

        fp2 = open(output_file, "w")
        fp2.write("*******************************************\n")
        fp2.write("          TICKET REPORT\n")
        fp2.write("\n*******************************************\n")
        fp2.write(f"\nThere are {num_tickets} tickets in the database.\n")
        fp2.write(f"\nMaximum Ticket price is ${max_price:.2f}.\n")
        fp2.write(f"Minimum Ticket price is ${min_price:.2f}.\n")
        fp2.write(f"Average Ticket Price is ${avg_price:.2f}.\n")
        fp2.write("\nThank you for using our ticket system!\n")
        fp2.write("\n*******************************************\n")
        print("Report generated successfully. Please check output.txt.")
    else:
        print("No valid ticket prices found.")