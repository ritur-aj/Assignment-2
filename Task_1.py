# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
#                   1. 	Takes an integer input from the user.
#                   2. 	Checks whether the number is even or odd using an if-else statement.
#                   3. 	Displays the result accordingly.


Number = int(input("Enter a number :- "))
if Number % 2==0:
    print(f"{Number} is a Even number. ")
else:
    print(f" {Number} is a odd number. ")

