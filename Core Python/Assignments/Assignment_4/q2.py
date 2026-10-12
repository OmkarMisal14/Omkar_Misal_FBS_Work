# 2. WAP to print all odd numbers until n.
num = int(input("Enter a number: "))
i =1
while(i<num+1):
    if(i%2!=0):
        print(i)
    i+=1