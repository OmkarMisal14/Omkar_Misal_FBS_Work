def add(*data):
    sum =0
    for var in data:
        sum+=var    
    return sum
res=add(10,20,40,30)
print(res)