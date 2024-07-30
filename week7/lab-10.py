'''
Travel Expense using GUI

The program will ask a user:
• Number of days on the trip
• Total amount of airfare, if any
• Conference charges, if any
• Lodging charges, per night
• Amount of taxi charges, if any per day
• Meal charges, per day

The application should calculate and display the following:
• Total expenses incurred by the businessperson.
• The total allowable expense for the trip.
• The amount saved by the businessperson if the expense were under the total allowed.
• The amount the businessperson has to pay out of pocket if the expense were above the
total.

Name: Lucy Finnerty
Date: 7/23/24
'''
from tkinter import*

# create window with name of Travel Expenses and a size of 300x300
window = Tk()
window.title("Travel Expenses")
window.geometry('300x300')

# labels and entry fields
labels_texts = [
    "Amount of Days: ", 
    "Cost of Airfare: ", 
    "Conference Charges: ", 
    "Lodging Charges (per night): ", 
    "Taxi Charges (per day): ", 
    "Meal Charges (per day): "
]

entries = [] # list to store entry fields
row = 0  # variable to keep track of current row for grid

# create and place labels/entry fields
for text in labels_texts:
    label = Label(window, text=text) # new label
    label.grid(column=0, row=row) # place at current row
    entry = Entry(window, width=20) # create entry field
    entry.grid(column=1, row=row) # place entry field next to label
    entries.append(entry) # store entry field in list
    row += 1 # increment to move to next row

# assign entries to variables
entry_days, entry_airfare, entry_conf_charges, entry_lodg_charges, entry_taxi_charges, entry_meal_charges = entries

# function to calculate total expenses, total allowable expenses, amount of money saved, and money paid out of pocket by user
def calculate_expenses():
    # get input values from entry fields - set them to new variables for calculations
    days = int(entry_days.get())
    airfare = float(entry_airfare.get())
    conf_charges = float(entry_conf_charges.get())
    lodg_charges = float(entry_lodg_charges.get()) * days
    taxi_charges = float(entry_taxi_charges.get()) * days
    meal_charges = float(entry_meal_charges.get()) * days
    # calculate total expenses by adding up all variables
    total_expense = airfare + conf_charges + lodg_charges + taxi_charges + meal_charges

    # calculate total allowable expenses according to the policy
    allowable_meal = min(meal_charges, 47 * days) # $47 per day for meals
    allowable_taxi = min(taxi_charges, 40 * days) # $40 per day for taxis
    allowable_lodging = min(lodg_charges, 195 * days) # $195 per day for lodging
    allowable_airfare = min(airfare, 600) # cannot exceed $600
    # calculate allowable_total by adding them all up
    allowable_total = allowable_meal + allowable_taxi + allowable_lodging + allowable_airfare + conf_charges
    
    # if total_expense is less than or equal to allowable_total, then calculate amount_saved
    if total_expense <= allowable_total:
        amount_saved = allowable_total - total_expense
        amount_out_of_pocket = 0 # no money paid out of pocket
    else: # user did not save any money, calculate money paid out_of_pocket
        amount_saved = 0
        amount_out_of_pocket = total_expense - allowable_total
        
    # display results to user
    result_total_expense.configure(text=f"Total Expenses: ${total_expense:.2f}")
    result_allowable_expense.configure(text=f"Total Allowable Expense: ${allowable_total:.2f}")
    result_amount_saved.configure(text=f"Amount Saved: ${amount_saved:.2f}")
    result_amount_out_of_pocket.configure(text=f"Out of Pocket: ${amount_out_of_pocket:.2f}")

# calculate button for when user has input numbers for all fields
calculate_button = Button(window, text="calculate", command=calculate_expenses)
calculate_button.grid(column=1, row=6, pady=10)

# result labels
result_total_expense = Label(window, text="")
result_total_expense.grid(column=0, row=row+1, columnspan=2)

result_allowable_expense = Label(window, text="")
result_allowable_expense.grid(column=0, row=row+2, columnspan=2)

result_amount_saved = Label(window, text="")
result_amount_saved.grid(column=0, row=row+3, columnspan=2)

result_amount_out_of_pocket = Label(window, text="")
result_amount_out_of_pocket.grid(column=0, row=row+4, columnspan=2)

# start the program
window.mainloop()