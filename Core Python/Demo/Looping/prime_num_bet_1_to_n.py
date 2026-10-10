# Prime numbers between 1 to n.
num = int(input("Enter a number: "))
if(num>1):
    for j in range(2, num+1):
        for i in range(2, j):
            if(j%i ==0):
                break
        else:
            print(j)
else:
    print("The give number is less then 2.")