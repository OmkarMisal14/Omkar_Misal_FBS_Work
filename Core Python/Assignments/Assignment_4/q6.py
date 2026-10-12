# 6. WAP to check if a given number is prime number or not.
num = int(input("Enter a number: "))
i= 2 
if num >2:
    while i<int(num**.5)+1:
        if(num%i==0):
            print("The given number is not a prime number.")
            break
        i+=1
    else:
        print("The given number is a prime number.")
else:
    print("The number is not a prime number.")