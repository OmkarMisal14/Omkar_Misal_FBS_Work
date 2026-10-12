# 10. WAP to check if given number is Perfect Number.
num = int(input("Enter a number: "))
i = 1
sum = 0
if num>0:
    while i<num:
        if num%i ==0:
            sum +=i
        i+=1
    if sum ==num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
else:
    print("The number is not a perfect number.")