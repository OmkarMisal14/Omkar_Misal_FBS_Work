data =[1,2,3,4,5,6]
res = list(filter(lambda num: num%2==0, data))
print(res)
res = list(filter(lambda num: num**2, data))
print(res)