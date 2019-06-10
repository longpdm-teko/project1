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

