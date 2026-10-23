data = [1,2,3,4,5,6]
# method 1
def sq(n):
    return n*n

print(list(map(sq, data)))
# method 2 
print(list(map(lambda n: n**2,data)))