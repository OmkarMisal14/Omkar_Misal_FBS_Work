# Write a program to swap two numbers using third variable.
num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))
temp = num1
num1 = num2
num2 = temp
print(f"New Altered numbers are num1:{num1} and num2:{num2}")