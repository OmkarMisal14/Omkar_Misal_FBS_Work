# * Traditional way 

newList =[]
for a in range(1, 11):
    newList.append(a**3)
print(newList)

# ! Comprehension way
newLi = [a**3 for a in range(1,11) ]
print(newLi)