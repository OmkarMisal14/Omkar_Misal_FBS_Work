# 11. WAP to check if given number Strong Number.
num = int(input("Enter a number: "))
temp = num 
sum = 0
while temp>0:
    d = temp%10
    fact =1
    for i in range(1,d+1):
        fact *=i
    sum +=fact
    temp //=10
print(sum)
if(sum == num):
    print("It is a strong number.")
else:
    print("It is not a strong number.")
