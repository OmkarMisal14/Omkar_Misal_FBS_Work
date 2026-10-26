# 1. Write a program to accept year from user and check if it is a leap year or not.
year = int(input("Enter a year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")