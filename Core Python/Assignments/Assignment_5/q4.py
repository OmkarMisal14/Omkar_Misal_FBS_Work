# 4. WAP to print Armstrong number within a given range
rang = int(input("Enter a range:"))
for i in range(2, rang+1):
    temp = i
    count = 0
    while i>0:
        i //=10
        count+=1
    total = 0
    i = temp
    while i>0:
        d = i%10
        total +=(d**count)
        i//=10
    if(total == temp):
        print(total)