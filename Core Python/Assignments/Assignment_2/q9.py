# Write a program to swap two numbers without using third variable.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num2 = num1+num2
num1 = num2-num1
num2 = num2-num1
print(type(num1))
print(f"Now num1 is {num1} and num2 is {num2}")