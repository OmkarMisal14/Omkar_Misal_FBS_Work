num = int(input())
temp = num 
count = 0
while(temp >0):
    temp//=10
    count+=1

print(count,"is the count")

temp = num
i = 1
while(i<=num):
    flag = temp%10
    count1 =count
    while(count1>0):
        print()