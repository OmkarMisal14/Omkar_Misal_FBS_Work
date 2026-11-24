li = [2,4,8,6,5]
newList=[]
for a in li:
    newList.append(a**2)
print(newList)

# ! Comprehension way
newLi = [a**2 for a in li]
print(newLi)