# 5. WAP to print Fibonacci series upto n.
num = int(input("Enter a number: "))
a = -1 #can also use 0 instead of -1
b = 1
c = 0
while num>0:
    c = a+b
    print(c)
    a = b
    b = c
    num-=1
    