# Python program to find the largest number among the three input numbers

print("LARGEST OF THREE")
num1 = 10
num2 = 14
num3 = 12

# Uncomment to use input
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

# Code to add two numbers
print("SUM OF TWO NUMBERS")
a = input('Enter first number: ')
b = input('Enter second number: ')
sum = float(a) + float(b)
print(f'The sum of {a} and {b} is {sum}')
