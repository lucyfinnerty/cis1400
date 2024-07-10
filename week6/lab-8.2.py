'''
Ticketing System using File I/O

This program should read tickets and prices from ticket.txt; find minimum, maximum, and
average ticket prices and output the report into a file called output.txt.

Name: Lucy Finnerty
Date: 7/9/24
'''

import os

# tickt.txt is the file this program will read
input_file = r'C:\git\cis1400\week6\ticket.txt'
# information / calculations will be written in output.txt
output_file = 'output.txt'

# check if path is not an existing file, then display error message
if not os.path.isfile(input_file):
    print(f"{input_file} not found!")
else: # path is an existing file
    fp = open(input_file,"r") # open input_file (ticket.txt) in read mode
    lines = fp.readlines() # read all lines into lines list
    # parse the ticket prices from the lines (skip header line)
    # split each line by spaces, takes the second element (the price), and converts it to a float
    ticket_prices = [float(line.split()[1]) for line in lines[1:] if line.strip()]

    # if list of ticket prices is not empty
    if ticket_prices:
        # calculate number of tickets, min, max, and average prices
        num_tickets = len(ticket_prices)
        max_price = max(ticket_prices)
        min_price = min(ticket_prices)
        avg_price = sum(ticket_prices) / num_tickets

        # open output_file (output.txt) in write mode
        fp2 = open(output_file, "w")
        # write headers and calculations to output.txt
        fp2.write("*******************************************\n")
        fp2.write("          TICKET REPORT\n")
        fp2.write("\n*******************************************\n")
        fp2.write(f"\nThere are {num_tickets} tickets in the database.\n")
        fp2.write(f"\nMaximum Ticket price is ${max_price:.2f}.\n")
        fp2.write(f"Minimum Ticket price is ${min_price:.2f}.\n")
        fp2.write(f"Average Ticket Price is ${avg_price:.2f}.\n")
        fp2.write("\nThank you for using our ticket system!\n")
        fp2.write("\n*******************************************\n")
        # display success message to console to let user know it worked
        print("Report generated successfully. Please check output.txt.")
    else: # list of ticket prices is empty, display following message
        print("No valid ticket prices found.")