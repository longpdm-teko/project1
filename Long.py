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

    # Write a Python program to print all even numbers from a given numbers list in the same order and stop
    # the printing if any numbers that come after 237 in the sequence
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958,743, 527
        ]
    for num in numbers:
        if num == 237:
           print(num)
           break;
        elif num % 2 == 0:
           print(num)

    # Write a Python program to add two objects if both objects are an integer type
    def add_numbers(a, b):
        if not (isinstance(a,int) and isinstance(b,int)):
            raise TypeError("Enter integers")
        return a + b
    print(add_numbers(4,6))

    # Write a Python program to find whether a given number (accept from the user) is even or odd
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    # Write a Python function that takes a sequence of numbers and determines if all the numbers are different
    # from each other.
    def distinct_test(data):
        if len(data) == len(set(data)):
            return True
        else:
            return False
    print(distinct_test([4, 2, 5, 4, 3]))

    # Write a Python program to check if a number is positive, negative or zero
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

    # Write a Python program to test whether a passed letter is a vowel or not
    def is_vowel(char):
        all_vowels = "aeiou"
        return char in all_vowels
    print(is_vowel("a"))

    # Write a Python program to solve (x + y) * (x + y)
    x = int(input("Enter value x: "))
    y = int(input("Enter value y: "))
    def equation_1(x, y):
        return (x + y) * (x + y)
    print(equation_1(x, y))

    # Write a Python program that will accept the base and height of a triangle and compute the area
    b = int(input("Input the base: "))
    h = int(input("Input the height: "))
    area_triangle = (b*h)/2
    print("The area of the triangle is ", area_triangle)

# Write a Python program to find the median among three given numbers
print("Enter three different numbers!")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
if y < x and x < z:
    print("The median is ", x)
elif z < x and x <y:
    print("The median is ", x)
elif x < y and y < z:
    print("The median is ", y)
elif z < y and y < x:
    print("The median is ", y)
elif x < z and z < y:
    print("The median is ", z)
elif y < z and z < x:
    print("The median is ", z)
















