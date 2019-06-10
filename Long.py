# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
first = input("Enter first name: ")
last = input("Enter last name: ")
print(last + " " + first)

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
numbers = input("Enter numbers separated by commas: ")
list = numbers.split (",")
tuple = tuple(list)
print(list)
print(tuple)

# Write a Python program to display the examination schedule
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)

# Write a Python program to calculate number of days between two dates.
from datetime import date
date_1 = date(2014,7,2)
date_2 = date(2014,7,11)
num_days = date_2 - date_1
print(num_days)

# Write a Python program to get the difference between a given number and 17
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        print("Enter a smaller number")
print(difference(18))