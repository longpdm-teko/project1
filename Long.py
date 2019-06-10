def test_data_structure():
    # Write a Python program which accepts the user's first and last name and print them in reverse order with a space
    # between them
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    print(last + " " + first)

    # Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
    # tuple with those numbers
    numbers = input("Enter numbers separated by commas: ")
    list = numbers.split(",")
    tuple = tuple(list)
    print(list)
    print(tuple)

    # Write a Python program to display the examination schedule
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : %i / %i / %i" % exam_st_date)

    # Write a Python program to calculate number of days between two dates.
    from datetime import date

    date_1 = date(2014, 7, 2)
    date_2 = date(2014, 7, 11)
    num_days = date_2 - date_1
    print(num_days)

    # Write a Python program to get the difference between a given number and 17
    def difference(n):
        if n <= 17:
            return 17 - n
        else:
            print("Enter a smaller number")

    print(difference(18))

# Write a Python program which accepts the radius of a circle from the user and compute the area
from math import pi
r = float(input("Input the radius : "))
print ("The area of the circle is " + str(pi*r**2))

# Write a Python program to display the first and last colors
color_list = ["Red", "Green", "White", "Black"]
print("%s %s" % (color_list[0], color_list[-1]))

# Write a Python program to print the calendar of a given month and year
import calendar
Y = int(input("Enter the year: "))
M = int(input("Enter the month: "))
print(calendar.month(Y, M))

# Write a Python program to print out a set containing all the colors from color_list_1 which are not present
# in color_list_2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

# Write a Python program that will accept the base and height of a triangle and compute the area
b = int(input("Enter the base : "))
h = int(input("Enter the height: "))
area = (b*h)/2
print(area)