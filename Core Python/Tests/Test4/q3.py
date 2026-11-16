# 3. WAP to print following patterns
def zPattern(num):
    print("*"*num)
    for i in range(1, num-1):
        print(" "*(num-1-i)+"*")
    print("*"*num)

n = 5
zPattern(n)
