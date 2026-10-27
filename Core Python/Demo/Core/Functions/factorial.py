def fact(num):
    multi= 1
    for i in range(num, 1, -1):
        multi*=i
    return multi

n = int(input("Enter a number: "))
print(fact(n))