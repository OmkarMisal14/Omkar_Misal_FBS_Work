def seq(n, sum):
    if(n<1):
        # print(sum)
        return sum
    print(n)
    sum+=n
    return seq(n-1,sum)
res = seq(5, 0)
print(res)

