#  12. Write a program to check if given number is Armstrong number or not.
num = int(input("Enter a number:"))
temp = num
count = 0
while temp>0:
    count+=1
    temp//=10
temp = num
sum = 0
while temp>0:
    d = temp%10
    d**=count
    sum+=d
    temp//=10
if num==sum:
    print("The number is armstrong number.")
else:
    print("The number is not armstrong number.")