def add(*data):
    sum =0
    for var in data:
        sum+=var  
    print(type(data))  
    return sum
res=add(10,20,40,30)
print(res)