# Task 2: Sum of Integers from 1 to 50 Using a Loop
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

number_1 = int(input("Enter first number : "))
number_2 = int(input("Enter second number : "))

Sum = 0    #<--------------------------------<
for i in range(number_1,number_2+1 ):       #|----------------This Sum +=i formula add Sum value to (Sum = 0) one by one.
    Sum +=i   # >---------------------------^
    # print(i)


print(f"Sum of {number_1} and {number_2} is  : {Sum} ")