'''
Positive Negative Calculator

This program will allow a user to input as many numbers as they would like (positive and/or negative).
Then it will count how many positives and negatives there are, the total sum of the numbers the user
inputs, and the average of the numbers.

Name: Lucy Finnerty
Date: 7/3/24
'''

'''
this function takes the number of iterations (num_loops) as an input. It prompts the user to enter a 
number in each iteration and counts number of positive numbers and negative numbers, total sum of 
the numbers, and their average.

parameter: num_loops - the number of numbers the user will input
return: pos_count, neg_count, sum
'''
def calculator(num_loops):
    # initialize counts and sum
    count = 1
    pos_count = 0
    neg_count = 0
    sum = 0

    # while count is less than amount numbers user wants to enter (num_loops)...
    while count <= num_loops:
        num = float(input(f"{count}. Enter Number: ")) # number user enters for calculations

        # if user's number is greater than 0 --> positive
        if num > 0:
            pos_count += 1 # increment pos_count
        # else if user's number is less than 0 --> negative
        elif num < 0:
            neg_count += 1 # increment neg_count
        
        # add user's number to total sum
        sum += num
        # increment count to be compared to num_loops
        count += 1
    # return results    
    return pos_count, neg_count, sum

'''
This function initiates the main program, calls the calulator function, calculates the average, 
displays results, and asks if the user wants to use the calculator again.
'''
def main():
    num_loops = None # the number of numbers user wants to input (number of loops)
    # while num_loops is null, loop runs indefinitely until user inputs positive integer
    while num_loops is None:
        # ask user for how many numbers they want to input into calculator
        num_loops = int(input("How many numbers would you like to enter? "))
        # ensure the user inputs a positive value
        if num_loops <= 0:
            print("The number of inputs must be a positive number!\n")
            num_loops = None
            
    # get the counts and sum from calculator function
    pos_count, neg_count, sum = calculator(num_loops)
    # calculate average
    average = sum / num_loops

    # display results
    print(f"\nThe number of positives is {pos_count}")
    print(f"The number of negatives is {neg_count}")
    print(f"The total is {sum:.2f}")
    print(f"The average is {average:.2f}\n")

    # loop runs indefinitely until user enters valid input, then those actions are taken and loop breaks.
    # if they enter invalid input then loop continues, prompting the user for valid input (yes or no)
    while True:
        # ask user if they would like to use the calculator again
        repeat = input("Would you like to repeat (Enter yes or no): ")

        # if user replies 'yes'...
        if repeat == "yes" or repeat == "Yes":
            print("\n")
            main() # repeat main function
            break
        # if user replies 'no'...
        elif repeat == "no" or repeat == "No":
            print("\nThank you for using the Positive Negative Calculator!") # display closing statement
            break
        else:
            print("Invalid input.") # let user know they entered invalid input

# run the main function
if __name__ == "__main__":
    main()