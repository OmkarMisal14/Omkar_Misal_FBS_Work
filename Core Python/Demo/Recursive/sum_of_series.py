def sOS(n):
    if(n<1):
        return n
    return n+sOS(n-1)

print(sOS(5))