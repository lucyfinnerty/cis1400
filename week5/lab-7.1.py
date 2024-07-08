'''
Number Analysis Program

A program that asks the user to enter a series of 5 numbers. The program should store the
numbers in an array/list. Then it should find and output the lowest number, highest number, 
the total of the numbers in the array, and the average of the numbers in the array. 

Name: Lucy Finnerty
Date: 7/8/24
'''
# list that will contain user's number
numbers_list = []
# variable that ensures user can only input 5 numbers
count = 5

# while count does not equal 0, user will be asked to input a number
while count != 0:
    num = int(input("Please input five numbers: "))
    # number will be be added to end of list
    numbers_list.append(num)
    # decrement count so loop can end once count = 0
    count -= 1

# function that finds the smallest number in numbers_list
def min_num():
    # initialize minimum value to first element of list
    min_val = numbers_list[0]
    # iterate through the list
    for num in numbers_list:
        # if num from numbers_list is less than min_val...
        if num < min_val:
            # num is the new min_val
            min_val = num
    return min_val

# function that finds the largest number in numbers_list
def max_num():
    # initialize maximum value to first element of list
    max_val = numbers_list[0]
    # iterate through the list
    for num in numbers_list:
        # if num from numbers_list is greater than max_val...
        if num > max_val:
            # num is the new max_val
            max_val = num
    return max_val
        
# function that adds up all of the numbers in numbers_list
def total():
    # initialize sum to 0
    sum = 0
    # iterate through the list
    for num in numbers_list:
        # for every num in the list, add to sum
        sum += num
    return sum

# function that calculates the average of the numbers in numbers_list
def average(sum):
    # divide sum by the length of the list (5)
    return sum / len(numbers_list)

# display results
print("Your list of numbers:", numbers_list)
total_sum = total()
print("The minimum number is", min_num())
print("The maximum number is", max_num())
print("The total is", total_sum)
print("The average is", average(total_sum))