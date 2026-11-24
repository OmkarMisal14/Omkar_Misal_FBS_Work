# * Traditional way
li = []

for i in range(1,4):
    for j in range(1,4):
        t = (i,j)
        li.append(t)

print(li)

# ! Nested Comprehension way 
newLi = [[i,j] for i in range(1, 4) for j in range(1,4)]
print(newLi)