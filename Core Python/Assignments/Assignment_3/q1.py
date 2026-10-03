# 1. Write a program to check if the given number is positive or negative.

num = int(input("Enter a number: "))
if(num>0):
    print(f"The number {num} is positive")
elif(num==0):
    print(f"The number {num} is neutral")
else:
    print(f"The number {num} is negative")