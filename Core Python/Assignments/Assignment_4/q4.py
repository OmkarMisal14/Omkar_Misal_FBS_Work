# 4. WAP to print factorial of a number .
num = int(input("Enter a number: "))
i = 0
fctoral = 1
while num>0:
    fctoral*=num
    num-=1
    print(num)

print(f"The factorial of a number is {fctoral}")