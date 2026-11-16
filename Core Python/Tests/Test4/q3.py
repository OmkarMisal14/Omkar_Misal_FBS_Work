# 3. WAP to print following patterns
def zPattern(num):
    print("*"*num)
    for i in range(1, num+1):
        print(" "*(num-i)+"*")
    print("*"*num)

n = 20
zPattern(n)
