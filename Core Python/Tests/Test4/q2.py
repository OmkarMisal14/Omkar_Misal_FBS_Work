# 2. Write a program to find factorial of given number using recursion
def recursion(num):
    if(num ==1 or num ==0):
        return 1
    return num* recursion(num-1)


num = int(input("Enter a number: "))
print("Factorial of given number is", recursion(num))
