'''
Distance from the Average Calculator

This program allows a user to enter as many numbers as they would like. Then the 
average of the numbers will be calculated and subtracted from each number to find 
the distance. The user may stop entering numbers by inputting -9999. This will not 
work if they have not entered at least one number.

Name: Lucy Finnerty
Date: 7/8/24
'''

# list that will contain user's numbers
numbers_list = []

# user can enter as many numbers as they would like, until they enter -9999 to stop
while True:
    # user's number converted to an integer
    num = int(input("Please enter a number (-9999 to stop): "))
    # user cannot quit without entering a number
    if num == -9999 and len(numbers_list) == 0:
        print("\nYou must enter at least one value!\n")
    # loop breaks if user has entered a number/s and enters -9999
    elif num == -9999 and len(numbers_list) > 0:
        break
    # number is added to end of the list
    else:
        numbers_list.append(num)

# function that calculates the distance from a number to the average of all inputted numbers
def distance():
    # call average function, store result in avg
    avg = average(total_sum)
    # iterate through list
    for num in numbers_list:
        # distance is set to the result of avg subtracted from num
        dist = round(num - avg)
        # display distance result
        print(f"The distance between {num} and the average {avg} is {dist}.")

# function that adds up all of the numbers in numbers_list
def total():
    # initialize sum to 0
    sum = 0
    # iterate through the numbers_list
    for num in numbers_list:
        # for every num in the numbers_list, add to sum
        sum += num
    return sum

# function that calculates the average of the numbers in numbers_list
def average(sum):
    # divide sum by the length of the numbers_list
    return round(sum / len(numbers_list))

# calculate total
total_sum = total()
# display numbers_list and average using total_sum
print(f"\nThe numbers you entered are {numbers_list} and the average is {average(total_sum)}.\n")
# call distance funtion for calculations
distance()