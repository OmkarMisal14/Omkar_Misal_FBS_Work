# 6. Write a program to print first n prime numbers.
n = int(input("Enter n number: "))
i = 2
while i<=n:
    for j in range(2, int(i**0.5)+1):
        if(i%j==0):
            break
    else:
        print(i)
    i+=1


    